from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

from .forms import ProductForm

def all_products(request):
    products = Product.objects.all()
    query = None
    categories = None
    types = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'name'  
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'type' in request.GET:
            types = request.GET.getlist('type')  # Get a list of all selected types
            # Filter products based on selected types
            products = products.filter(category__type__in=types).distinct()

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Uh oh! It seems like you forgot to type something in the search bar.")
                return redirect('products')

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_types': types,
        'current_sorting': current_sorting,
    }
    
    return render(request, 'products/products.html', context)




def product_detail(request, product_id):
    """A view that will show the user all the details of a product once pressed. """

    products = get_object_or_404(Product, pk=product_id)

    context = {
        'product': products,
    }
    
    return render(request, 'products/product_detail.html', context)



def add_product(request):
    """ Add a product to the store """
    form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)