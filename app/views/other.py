from django.shortcuts import render


def index_view(request):
    return render(request, 'app/index.html')


def item_view(request):
    return render(request, 'app/item.html')
