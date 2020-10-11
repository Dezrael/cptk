from django import forms

from .models import Product, Orders

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {'title', 'category', 'manufacturer', 's_description',
                  'description', 'img', 'price'}

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = {'first_name', 'last_name', 'email', 'address',
                  'comment'}

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)