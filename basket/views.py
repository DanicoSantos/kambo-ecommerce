from django.http import JsonResponse, response
from django.shortcuts import get_object_or_404, render

from basket.basket import Basket

from store.models import Product


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_quantity = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, quantity=product_quantity)
        basket_quantity = basket.__len__()
        response = JsonResponse({'qty': basket_quantity})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'delete':
        product_id = int(request.POST.get('productid'))
        basket.delete(product_id=product_id)

        basket_quantity = basket.__len__()
        basket_total = basket.get_total_price()
        response = JsonResponse(
            {'quantity': basket_quantity, 'subtotal': basket_total})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'update':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product_id=product_id, quantity=product_qty)

        basket_quantity = basket.__len__()
        basket_total = basket.get_total_price()
        response = JsonResponse(
            {'quantity': basket_quantity, 'subtotal': basket_total})
        return response
