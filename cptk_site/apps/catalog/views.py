from django.shortcuts import render, redirect
from .models import Attribute, Attribute_list, Category, ProductImages, Product, Orders, ProductFiles
from .forms import ProductForm, OrderForm

from rest_framework.response import Response
from rest_framework.views import APIView

import json
# Create your views here.


def catalog(request):
    categories = Category.objects.filter(parent = None)
    return render(
        request,
        'catalog/catalog.html',
        context = {'categories': categories}
    )

def category(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    children = Category.objects.filter(parent = category)
    if len(children) > 0:
        return render(
            request,
            'catalog/category.html',
            context = {'category': category, 'children': children}
        )
    else:
        products = Product.objects.filter(category = category)
        return render(
            request,
            'catalog/products.html',
            context = {'category': category, 'products': products}
        )

def cart(request):
    return render(
        request,
        'catalog/cart.html'
    )

def products(request):
    products = Product.objects.all()
    return render(
        request,
        'catalog/products.html',
        context = {'products': products}
    )

def product(request, slug):
    product = Product.objects.get(slug__iexact=slug)
    return render(
        request,
        'catalog/product.html',
        context = {'product': product}
    )

def make_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order_f = form.save(commit=False)
            items = json.loads(request.POST['products'])
            products = ''
            for product in items:
                products += '\"' + product['title'] + '\" x' + str(product['count']) + ' (' + str(product['price']) + ' руб.) \n'
            order_f.products = products
            order_f.total_price = request.POST.get('total')
            order_f.save()
            return redirect('home')
        else:
            return render(
                request,
                'catalog/make_order.html',
                context = {'form': form, 'error': 'Введите корректные данные'}
            )
    else:
        form = OrderForm()
        return render(
            request,
            'catalog/make_order.html',
            context = {'form': form}
        )

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            post_f = form.save(commit=False)
            attributes = Attribute.objects.filter(category = post_f.category)
            post_f.save()

            for image in request.FILES.getlist('images'):
                pr_image = ProductImages(product = post_f, image = image)
                pr_image.save()

            for file in request.FILES.getlist('files'):
                pr_file = ProductFiles(product = post_f, file = file)
                pr_file.save()

            for attribute in attributes:
                attr = Attribute_list(attribute = attribute, product = post_f, value = request.POST.get('attr_{id}'.format(id=attribute.id) , 0))
                attr.save()

            return redirect('add_product')
        else:
            return render(
                request,
                'catalog/add_product.html',
                context = {'form': form, 'error': 'Введите корректные данные'}
            )
    else:
        form = ProductForm()
        return render(
            request,
            'catalog/add_product.html',
            context = {'form': form}
        )


class GetAttributesView(APIView):
    def get(self, request):
        category_id = request.query_params['category']
        category = Category.objects.get(id = category_id)
        attributes = [{'id': x.id, 'title': x.title.title, 'measure': x.measure.measure } for x in Attribute.objects.filter(category = category)]
        return Response(attributes)