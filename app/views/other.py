from django.shortcuts import render

from app.models import Item


def index_view(request):
    items = Item.objects.all()

    query = request.GET.get('query', '')
    if query:
        items = Item.objects.filter(type__exact=query)

    context = {
        'items': items
    }
    return render(request, 'app/index.html', context)


def item_view(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item
    }
    return render(request, 'app/item.html', context)
