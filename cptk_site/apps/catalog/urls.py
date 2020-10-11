from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('add_product', views.add_product, name='add_product'),
    path('cart', views.cart, name='cart'),
    path('make_order', views.make_order, name='make_order'),
    path('products', views.products, name='products'),
    path('api/get_attributes', views.GetAttributesView.as_view()),
]
