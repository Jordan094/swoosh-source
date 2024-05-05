from django.shortcuts import render, redirect, reverse, HttpResponse

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


def remove_from_bag(request, item_id):
    """ Remove the specified product from the shopping bag """

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        # Remove the item from the bag using pop
        bag.pop(item_id, None)

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))  # Redirect to the bag view


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product in the shopping bag """

    if request.method == 'POST':
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity'))
        print("Size:", size)
        print("Quantity:", quantity)
        bag = request.session.get('bag', {})
        

        # Check if the item exists in the bag
        if item_id in bag:
            # If the item has size variations
            if isinstance(bag[item_id], dict):
                # Update the quantity of the specified size
                if size in bag[item_id]:
                    # Update the quantity directly instead of adding to the existing quantity
                    bag[item_id][size] = quantity
                    # Remove the size if the new quantity is zero or negative
                    if bag[item_id][size] <= 0:
                        del bag[item_id][size]
                        # If all sizes are removed, delete the item from the bag
                        if not bag[item_id]:
                            del bag[item_id]
                else:
                    # If the specified size doesn't exist, add it to the bag
                    bag[item_id][size] = quantity
            else:
                # If the item doesn't have size variations yet, create a size dictionary and add the quantity
                bag[item_id] = {size: quantity}
        else:
            # If the item doesn't exist in the bag, add it with the new size and quantity
            bag[item_id] = {size: quantity}

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))  # Redirect to the bag view