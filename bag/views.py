from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """A view to return the shopping bag """
    
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """This adds a quantity of the specified item to the bag"""

    quantity = int(request.POST.get('quantity'))
    size = int(request.POST.get('size'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in bag:
        if isinstance(bag[item_id], dict) and size in bag[item_id]:
            bag[item_id][size] += quantity
        else:
            bag[item_id][size] = quantity
    else:
        bag[item_id] = {size: quantity}


    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)