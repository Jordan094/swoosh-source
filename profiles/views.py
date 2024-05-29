from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

@login_required
def profile(request):
    """ Display the user's profile. """
    # Get the user's profile object or return a 404 if not found
    profile = get_object_or_404(UserProfile, user=request.user)

    # Check if the request is a POST request (i.e., form submission)
    if request.method == 'POST':
        # Create a form instance with the submitted data and the user's profile
        form = UserProfileForm(request.POST, instance=profile)
        # Validate the form
        if form.is_valid():
            # Save the valid form data to the profile
            form.save()
            # Display a success message
            messages.success(request, 'Your profile has been updated successfully.')
        else:
            # Display an error message if the form is invalid
            messages.error(request, 'Failed to update your profile. Please check the form for errors and try again.')
    else:
        # If not a POST request, create a form instance with the user's profile
        form = UserProfileForm(instance=profile)
    
    # Get all orders related to the user's profile
    orders = profile.Orders.all()

    # Specify the template to render
    template = 'profiles/profile.html'
    # Context data to pass to the template
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    # Render the template with the context data
    return render(request, template, context)

def order_history(request, order_number):
    """ Display the user's order history. """
    # Get the order object by order number or return a 404 if not found
    order = get_object_or_404(Order, order_number=order_number)

    # Display an informational message about the past order
    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date. You can find the order details below.'
    ))

    # Specify the template to render
    template = 'checkout/checkout_success.html'
    # Context data to pass to the template
    context = {
        'order': order,
        'from_profile': True,
    }

    # Render the template with the context data
    return render(request, template, context)
