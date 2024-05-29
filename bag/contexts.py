from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def bag_contents(request):
    # Initialize variables
    bag_items = []
    total = Decimal(0)
    product_count = 0
    bag = request.session.get('bag', {})

    # Loop through bag items
    for item_id, item_data in bag.items():
        # Get product object
        product = get_object_or_404(Product, pk=item_id)
        # Convert price to Decimal
        price = Decimal(str(product.price))
        if isinstance(item_data, dict):
            # If item has multiple sizes
            for size, quantity in item_data.items():
                # Calculate item total
                item_total = price * Decimal(quantity)
                # Add item total to overall total
                total += item_total
                # Append item details to bag_items list
                bag_items.append({
                    'item_id': item_id,
                    'size': size,
                    'quantity': quantity,
                    'product': product,
                    'price': price,
                    'item_total': item_total,
                })

    # Calculate delivery cost
    delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    # Calculate grand total
    grand_total = delivery + total

    # Create context dictionary
    context = {
        'bag_items': bag_items,
        'delivery': delivery,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
