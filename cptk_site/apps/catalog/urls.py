from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('category/<slug>', views.category, name='category'),
    path('products', views.products, name='products'),
    path('products/<slug>', views.product, name='product'),
    path('add_product', views.add_product, name='add_product'),
    path('cart', views.cart, name='cart'),
    path('make_order', views.make_order, name='make_order'),
    path('api/get_attributes', views.GetAttributesView.as_view()),
]
