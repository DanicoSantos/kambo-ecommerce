from django.shortcuts import render

from .models import Category, Product


def home_page(request):
    products = Product.objects.all()
    context = dict(products=products)
    return render(request, 'store/index.html', context)


def products_list(request):
    products = Product.objects.all()
    context = dict(products=products)
    return render(request, 'store/shop.html', context)


def product_details(request):
    return render(request, 'store/product-details.html')


def shop_cart(request):
    return render(request, 'store/shop-cart.html')