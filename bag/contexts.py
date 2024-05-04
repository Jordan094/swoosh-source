from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    bag_items = []
    total = Decimal(0)
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        price = Decimal(str(product.price))
        if isinstance(item_data, dict):
            for size, quantity in item_data.items():
                item_total = price * Decimal(quantity)
                total += item_total
                bag_items.append({
                    'item_id': item_id,
                    'size': size,
                    'quantity': quantity,
                    'product': product,
                    'price': price,
                    'item_total': item_total,
                })

    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'delivery': delivery,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context