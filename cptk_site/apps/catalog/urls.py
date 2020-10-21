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
    path('api/get_sel_attributes', views.GetSelectableAttributesView.as_view()),
    path('edit/<int:id>/', views.edt_product, name='edit'),
    path('delite/<int:id>/', views.del_product, name='delite')
]
