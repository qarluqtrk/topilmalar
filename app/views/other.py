from django.shortcuts import render

from app.models import Item


def index_view(request):
    items = Item.objects.all()
    return render(request, 'app/index.html',
                  context={'items': items})


def item_view(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'app/item.html'
                  , context={'item': item})



