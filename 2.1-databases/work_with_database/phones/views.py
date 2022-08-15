from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting_mode = request.GET.get('sort')
    phones = Phone.objects.all()
    if sorting_mode == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sorting_mode == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sorting_mode == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones = Phone.objects.filter(slug=slug)
    phone = phones[0]
    context = {
        'phone': phone
    }
    return render(request, template, context)

