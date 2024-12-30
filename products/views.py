from django.shortcuts import render
from .models import Product
# Create your views here.


def home(request):
    featured_products = Product.objects.all()
    context = {'featured_products': featured_products}

    return render(request, 'home.html', context)


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'product_detail.html', {'product': product})
