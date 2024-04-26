from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.


def all_products(request):
    """A view that will show the user all of the products on the site """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view that will show the user all the details of a product once pressed. """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }
    
    return render(request, 'products/product_detail.html', context)