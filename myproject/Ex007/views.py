from django.shortcuts import render
from . import forms
from Ex007.models import Order, Client, Good
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta

def good_update(request):
    if request.method == 'POST':
        form = forms.GoodUpdate(request.POST)
        if form.is_valid():
            pk = form.cleaned_data['pk']
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            good = Good.objects.filter(pk=pk).first()
            if good is not None:
                good.name = name
                good.description = description
                good.price = price
                good.quantity = quantity
                good.save()
                message = 'Товар изменён'
            else:
                message = 'Проверьте данные товара'
    else:
        form = forms.GoodUpdate()
        message = 'Введите данные'
    return render(request, 'Ex007/good_update.html', {'form': form, 'message': message})

def good_image(request):
    if request.method == 'POST':
        form = forms.GoodImage(request.POST, request.FILES)
        if form.is_valid():
            pk = form.cleaned_data['pk']
            image = form.cleaned_data['image']
            good = Good.objects.filter(pk=pk).first()
            if good is not None:
                good.picture = image
                good.save()
                message = 'Фото добавлено'
            else:
                message = 'Проверьте данные товара'
    else:
        form = forms.GoodImage()
        message = 'Добавьте фото'
    return render(request, 'Ex007/good_image.html', {'form': form, 'message': message})


def client_orders_by_time(request, client_id):
    goods = {7:[], 30:[], 365:[]}
    client = get_object_or_404(Client, pk=client_id)
    orders_7 = Order.objects.filter(client = client).filter(reg_data__gte = timezone.now().date() - timedelta(days=7))
    orders_30 = Order.objects.filter(client = client).filter(reg_data__gte = timezone.now().date() - timedelta(days=30))
    orders_365 = Order.objects.filter(client = client).filter(reg_data__gte = timezone.now().date() - timedelta(days=365))
    for order in orders_7:
        goods[7].append(order.good.all())
    for order in orders_30:
        goods[30].append(order.good.all())
    for order in orders_365:
        goods[365].append(order.good.all())
    return render(request, 'Ex007/client_orders_by_time.html', {'client': client.name, 'goods': goods})


def client_orders(request, client_id):
    goods = {}
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client = client)
    for order in orders:
        goods[order] = order.good.all()
    return render(request, 'Ex007/client_orders.html', {'client': client.name, 'goods': goods})