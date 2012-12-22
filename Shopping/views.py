from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404

from Shopping.models import Item
from Shopping.models import Store

def index(request):
    items = Item.objects.all().order_by('name')
    return render_to_response('shopping/index.html', { 'shopping_items': items})

def add(request):
    return HttpResponse("Wanna add eh!")

def item(request, item_id):
    i = get_object_or_404(Item, pk=item_id)
    return render_to_response('shopping/itemdetail.html', {'item': i})
