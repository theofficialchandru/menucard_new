from django.shortcuts import render ,redirect
from hotel.models import *

# Create your views here.


def menu_card(request):
    hotel_identifier = request.GET.get('hotel_id')
    menu_items = MenuItem.objects.all()
    # menu_items = MenuItem.objects.filter(category__hotel_users__user=request.user)
    categories = Category.objects.all()
    # categories = Category.objects.filter(hotel_users__user=request.user)
    properties = HotelUsers.objects.filter(user=request.user)
    return render(request, 'frontend/menu_card.html', {'menu_items': menu_items, 'categories': categories,'properties':properties,})



# availability 

def toggle_availability(request, pk):
    menu_item = MenuItem.objects.get(pk=pk)
    menu_item.available = not menu_item.available
    menu_item.save()
    return redirect('menu_list')  


