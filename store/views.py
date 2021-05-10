from django.shortcuts import render

from .models import Category, Product

def products_list(request):
    products = Product.objects.all()
    context = dict(products=products)
    return render(request, 'store/index.html', context)
