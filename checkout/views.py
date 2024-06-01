from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from django.contrib.auth.models import User
from profiles.forms import UserProfileForm
from .models import UserProfile
from bag.contexts import bag_contents

from .forms import OrderFeedbackForm

import stripe
import json

@require_POST
def cache_checkout_data(request):
    try:
        # Extracting PaymentIntent ID from client secret
        pid = request.POST.get('client_secret').split('_secret')[0]
        # Setting up Stripe API key
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # Modifying PaymentIntent with metadata
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user.username if request.user.is_authenticated else 'AnonymousUser',
        })
        return HttpResponse(status=200)  # Successfully cached checkout data
    except Exception as e:
        # Error handling for payment issue
        messages.error(request, 'Sorry there is an issue with your payment, please try again later.')
        return HttpResponse(content=e, status=400)  # Returning error response

def checkout(request):
    # Retrieving Stripe keys from settings
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # Handling POST request for checkout
        bag = request.session.get('bag', {})
        # Creating form data from POST request
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        # Creating order form with form data
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Saving order
            order = order_form.save()
            # Extracting PaymentIntent ID from client secret
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()
            # Creating order line items from bag
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        # If the item_data is an integer, it means it's a quantity without sizes
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data.items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    # Error handling for product not found in database
                    messages.error(request, "One of the products in your bag wasn't found in our database. Please call us for assistance!")
                    order.delete()  # Deleting incomplete order
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))  # Redirecting to checkout success page
        else:
            # Error handling for invalid form data
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                # Pre-filling order form with user's profile data
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'country': profile.default_country,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'county': profile.default_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    # Check if the user is authenticated before accessing the profile
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! Your order number is {order_number}. A confirmation email will be sent to {order.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


from django.shortcuts import redirect

@login_required
def order_feedback(request, order_id):
    order = get_object_or_404(Order, id=order_id, user_profile=request.user.userprofile)
    if request.method == 'POST':
        form = OrderFeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.order = order
            feedback.user_profile = request.user.userprofile
            feedback.save()
            return redirect('feedback_success')  # Corrected redirect to the view name
    else:
        form = OrderFeedbackForm()
    return render(request, 'checkout/order_feedback.html', {'form': form, 'order': order})

def feedback_success(request):
    return render(request, 'checkout/feedback_success.html')
