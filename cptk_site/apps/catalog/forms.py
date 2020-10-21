from django import forms

from mptt.forms import TreeNodeChoiceField

from .models import Product, Orders, Category


from ckeditor.widgets import CKEditorWidget
class CategoryForm(forms.ModelForm):
	title = forms.CharField(
		label=("Наименование:"),
		help_text=("Максимум 90 символов."),
		required=True,
	)
	hidden = forms.BooleanField(
		label=("Скрыть категорию:"),
		help_text=("Пользователи не увидят данную категорию и все товары в ней."),
		required=False,
	)
	svg = forms.CharField(
		widget=forms.Textarea,
		label=("SVG Картинка:"),
		help_text=("Картинка, которая используется для меню. <b>Вставить код SVG</b>"),
		required=False,
	)
	description = forms.CharField(
		widget=CKEditorWidget(),
		label=("Описание:"),
		required=False,
	)
	class Meta:
		model = Category
		fields = {'title', 'parent', 'description', 'svg', 'img', 'hidden',}



class ProductForm(forms.ModelForm):
	title = forms.CharField(widget=forms.TextInput(attrs={'autocomplete':'off'}))
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