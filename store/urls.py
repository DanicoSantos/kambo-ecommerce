from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('shop', views.shop, name='shop'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    
]
