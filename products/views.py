from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.

def all_products(request):
    """A view that will show the user all of the products on the site """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                message.error(request, "Uh oh! It seems like you forgot to type something in the search bar.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }
    
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """A view that will show the user all the details of a product once pressed. """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }
    
    return render(request, 'products/product_detail.html', context)