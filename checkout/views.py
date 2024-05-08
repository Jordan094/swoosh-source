from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty. Unable to Checkout")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51PEDwACLyXIvr5GTnysqSPdLxQ0DmNxSEpXlbeykaMVndnaOBhLF0hEka9TKXq9neUBPC4bAxtVvtbYOV6GaHDN600gEyOdP40',
        'client_secret' : 'test client secret',
    }

    return render(request, template, context)