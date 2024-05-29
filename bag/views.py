from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

def view_bag(request):
    """A view that renders the bag contents page"""
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """Add a quantity of the specified product to the shopping bag"""
    product = Product.objects.get(pk=item_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        size = request.POST.get('size')  
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

        if item_id in bag:
            if isinstance(bag[item_id], dict):  
                if size in bag[item_id]:  
                    bag[item_id][size] += quantity
                    messages.success(request, f'Added {product.name} to your bag')
                else:  
                    bag[item_id][size] = quantity
                    messages.success(request, f'Added {product.name} to your bag')
            else:  
                bag[item_id] = {size: quantity}
        else:  
            bag[item_id] = {size: quantity}
            messages.success(request, f'Added {product.name} to your bag')

        request.session['bag'] = bag
        return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id][size]
            if not bag[item_id]:
                bag.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product in the shopping bag"""

    if request.method == 'POST':
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity'))
        product = Product.objects.get(pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            if isinstance(bag[item_id], dict):
                if size in bag[item_id]:
                    bag[item_id][size] = quantity
                    messages.success(request, f'Updated quantity of: {product.name} to {quantity}')
                    if bag[item_id][size] <= 0:
                        del bag[item_id][size]
                        if not bag[item_id]:
                            del bag[item_id]
                else:
                    bag[item_id][size] = quantity
                    messages.success(request, f'Updated quantity of: {product.name} to {quantity}')
            else:
                bag[item_id] = {size: quantity}
        else:
            bag[item_id] = {size: quantity}

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))  
