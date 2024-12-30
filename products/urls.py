from django.urls import path
from .views import home, product_list, product_detail

urlpatterns = [
    path('', home, name='index'),
    path('products',product_list, name='product_list'),
    path('<slug:slug>', product_detail, name='product_detail'),
]