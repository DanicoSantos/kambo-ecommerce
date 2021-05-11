from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('shop', views.shop, name='shop'),
    path('shop-cart', views.shop_cart, name='shop_cart'),
    path('product-details', views.product_details, name='product_details'),
    
]
