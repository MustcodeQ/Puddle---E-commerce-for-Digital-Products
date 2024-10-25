# from django.shortcuts import render, get_object_or_404
# # Create your views here.


# from .models import Item
# #pressing the item you get the item detail 

# def detail(request, pk):
#     print(f"Requested item with pk: {pk}")
#     item = get_object_or_404(Item, pk=pk)
#     return render(request, 'item/detail.html', {'item': item})
#v-12
from django.shortcuts import render, get_object_or_404
from .models import Item

def detail(request, pk):
    print(f"Requested item with pk: {pk}")  # Check the requested pk
    item = get_object_or_404(Item, pk=pk)
    
    # Fetch related items based on the same category and not sold
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    
    print(f"Retrieved item: {item.name} with price {item.price}")  # Confirm the item fetched
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items  # Use the same name as in the template
    })

# This detail view function handles the logic for displaying the details of a 
# specific item and also shows a few related items that the user might be interested in.
#  It uses the item's primary key to find it in the database, and it also suggests other items 
# from the same category that are not yet sold. The debugging print statements help
#  track the flow of the request and the data being handled.(debugginh handling#)
