from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def home_page(request):
    products = Product.objects.all()
    context = dict(products=products)
    return render(request, 'store/index.html', context)


def categories(request):
    return {
        'categories': Category.objects.all()
    }


def shop(request):
    products = Product.objects.all()
    context = dict(products=products)
    return render(request, 'store/shop.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    context = dict(product=product)
    return render(request, 'store/products/detail.html', context)


def shop_cart(request):
    return render(request, 'store/shop-cart.html')
