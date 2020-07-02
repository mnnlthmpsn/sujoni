from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    categories = Category.objects.all()
    items = Item.objects.all()

    if items.count() > 4:
        recent_items = list(items[-4])
    else:
        recent_items = []
    return render(request, 'playground/index.html', {
        'categories': categories,
        'items': items
    })

def ac_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('playground:index'))

def add_item(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        cat = request.POST['category']
        category = Category.objects.get(title=cat)
        owner = request.POST['owner']
        title = request.POST['title']
        content = request.POST['content']

        if Item.objects.filter(title=title).exists():
            messages.add_message(request, messages.ERROR, 'Item already exists')
            return HttpResponseRedirect(reverse('playground:add_item'))
        else:
            item = Item(category=category, owner=owner, title=title, content=content)
            item.save()
            messages.add_message(request, messages.SUCCESS, 'Item Added')
            return HttpResponseRedirect(reverse('playground:index'))
           
    return render(request, 'playground/add_item.html', {'categories': categories})

def read_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    return render(request, 'playground/read_item.html', {'item': item})

def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        cat = request.POST['category']
        category = Category.objects.get(title=cat)
        owner = request.POST['owner']
        title = request.POST['title']
        content = request.POST['content']

        item.category = category
        item.owner = owner
        item.title = title
        item.content = content
        item.save()
        return HttpResponseRedirect(reverse('playground:read_item', kwargs={item_id: item_id}))
    return render(request, 'playground/edit_item.html', { 'item': item, 'categories': categories })