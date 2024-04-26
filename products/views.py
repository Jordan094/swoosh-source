from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    """A view that will show the user all of the products on the site """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)