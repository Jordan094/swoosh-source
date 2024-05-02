from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))
        size = request.POST.get('size')  # Retrieve size from POST data
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

        # Ensure bag[item_id] is an integer
        if item_id in bag:
            if isinstance(bag[item_id], dict):  # Check if the item is already in the bag
                if size in bag[item_id]:  # If the size already exists, update the quantity
                    bag[item_id][size] += quantity
                else:  # If the size doesn't exist, add it to the bag
                    bag[item_id][size] = quantity
            else:  # If the item exists but doesn't have size variations yet
                bag[item_id] = {size: quantity}
        else:  # If the item doesn't exist in the bag
            bag[item_id] = {size: quantity}

        request.session['bag'] = bag
        return redirect(redirect_url)