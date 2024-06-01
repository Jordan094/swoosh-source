from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from bag.views import remove_from_bag
from .models import Product, Category, UserProfile, Favourites
from .forms import ProductForm

def all_products(request):
    # Fetch all products initially
    products = Product.objects.all()
    query = None
    categories = None
    types = None
    sort = None
    direction = None

    if request.GET:
        # Handle sorting
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

        # Handle filtering by category
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # Handle filtering by type
        if 'type' in request.GET:
            types = request.GET.getlist('type')  # Get a list of all selected types
            products = products.filter(category__type__in=types).distinct()

        # Handle search queries
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Uh oh! It seems like you forgot to type something in the search bar.")
                return redirect('products')

            # Search in product name and description
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
    """ Show all the details of a product """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_to_favourites(request):
    if request.method == 'POST':
        try:
            product_id = request.POST.get('product_id')
            product = get_object_or_404(Product, pk=product_id)
            profile = request.user.userprofile

            if Favourites.objects.filter(user_profile=profile, favourite_item=product).exists():
                messages.error(request, 'Product is already in favorites.')
            else:
                Favourites.objects.create(
                    favourite_item=product,
                    user_profile=profile,
                )
                messages.info(request, 'Product added to favorites!')
        except Product.DoesNotExist:
            messages.error(request, 'Product does not exist.')
        except Exception as e:
            messages.error(request, str(e))

        redirect_url = request.POST.get('redirect_url', reverse('products'))
        return redirect(redirect_url)
    else:
        return redirect('products')

@login_required
def remove_from_favourites(request):
    if request.method == 'POST':
        try:
            product_id = request.POST.get('product_id')
            redirect_url = request.POST.get('redirect_url', reverse('products'))
            product = get_object_or_404(Product, id=product_id)
            profile = request.user.userprofile

            favourite = Favourites.objects.filter(user_profile=profile, favourite_item=product)
            if favourite.exists():
                favourite.delete()
                messages.info(request, 'Product removed from favorites!')
            else:
                messages.error(request, 'Product is not in favorites.')
        except Exception as e:
            messages.error(request, str(e))

        return redirect(redirect_url)
    else:
        return redirect('products')
