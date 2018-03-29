from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    list = List.objects.get(id=list_id)
    items = Item.objects.filter(list=list)

    return render(request, 'list.html', {'items': items})


def new_list(request):
    list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list)
    return redirect('/lists/%d/' % (list.id,))


def add_item(request, list_id):
    list = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list)
    return redirect('/lists/%d/' % (list.id,))
