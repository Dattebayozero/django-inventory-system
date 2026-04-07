from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'inventory/item_list.html' , {'items': items})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Item


def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk) 
    
    if request.method == "POST":
        item.name = request.POST.get('name')
        item.quantity = request.POST.get('quantity')
        item.price = request.POST.get('price')
        item.save()
        return redirect('/items/') 
        
    return render(request, 'inventory/edit_item.html', {'item': item})

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/items/')
    return render(request, 'inventory/delete_confirm.html', {'item': item})


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer

@api_view(['GET'])
def item_list_api(request):  
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def item_detail_api(request, pk):
    item = get_object_or_404(Item, pk=pk)
    serializer = ItemSerializer(item) 
    return Response(serializer.data)