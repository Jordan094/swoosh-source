from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):

    bag_items = []
    total = Decimal(0)
    product_count = 0
    bag = request.session.get('bag', {})

    print(request.session['bag'])
    

    for item_id, quantity in bag.items():        
        product = get_object_or_404(Product, pk=item_id)
        price = Decimal(str(product.price))
        print("Quantity type:", type(quantity))
        print("Price type:", type(price))
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'price': price,
        })
    
    total += quantity * product.price
        
    

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context