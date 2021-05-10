from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.products_list, name='products_list'),
    
]
