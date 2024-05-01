from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    
    print("Bag contents:", bag)  # Debug print to inspect the bag contents

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        quantity = item_data.get('quantity', 1)
        total += quantity * product.price
        product_count += quantity
        size = item_data.get('size', '')  # Fetch size data
        print("Item ID:", item_id, "Size:", size)  # Debug print to inspect size
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'size': size,  # Include size in bag items
        })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context


    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context