from django.shortcuts import render
from products.models import Product  # Adjust this import statement based on your actual app structure

def index(request):
    """A view to return the index page with random products"""
    # Retrieve three random products
    random_products = Product.objects.order_by('?')[:3]
    context = {
        'random_products': random_products
    }
    return render(request, 'home/index.html', context)
