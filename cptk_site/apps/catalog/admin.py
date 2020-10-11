from django.contrib import admin

# Register your models here.
from .models import Manufacturer, Category, Product, Attribute, Attribute_title, Attribute_measure, Attribute_list

class ManufacturerAdmin(admin.ModelAdmin):
	fields = ['title', 'image', 'description', 'link']
	list_display = ('title', 'link', 'slug')
	list_filter = ['title']
	search_fields = ['title']
	# prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
	fields = ['title', 'parent', 'description', 'svg', 'img', 'attr_list']
	list_display = ('title', 'parent')
	list_filter = ['title', 'parent']
	search_fields = ['title']


class AttributeAdmin(admin.ModelAdmin):
	fields = ['title', 'measure']
	list_display = ('title', 'measure')
	list_filter = ['title', 'measure']
	search_fields = ['title']


class Attribute_titleAdmin(admin.ModelAdmin):
	fields = ['title']
	list_display = ('title',)
	list_filter = ['title']
	search_fields = ['title']

class Attribute_measureAdmin(admin.ModelAdmin):
	fields = ['measure']
	list_display = ('measure',)
	list_filter = ['measure']
	search_fields = ['measure']


class Attribute_listAdmin(admin.ModelAdmin):
	fields = ['product_id', 'attribute_id', 'value']
	list_display = ('product_id', 'attribute_id', 'value')
	list_filter = ['product_id', 'attribute_id']
	search_fields = ['product_id', 'attribute_id']



admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Attribute, AttributeAdmin)
admin.site.register(Attribute_title, Attribute_titleAdmin)
admin.site.register(Attribute_measure, Attribute_measureAdmin)
