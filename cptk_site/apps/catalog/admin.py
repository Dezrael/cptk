from django.contrib import admin

# Register your models here.
from .models import Manufacturer, Category, Product, Attribute, Attribute_measure, Attribute_title, Attribute_list

class ManufacturerAdmin(admin.ModelAdmin):
	fields = ['title', 'image', 'description', 'link']
	list_display = ('title', 'link', 'slug')
	list_filter = ['title']
	search_fields = ['title']
	# prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
	fields = ['title', 'parent', 'description', 'svg', 'img', 'attr_list', 'selectable_attr_list']
	list_display = ('title', 'parent')
	list_filter = ['title', 'parent']
	search_fields = ['title']


class AttributeAdmin(admin.ModelAdmin):
	fields = ['title', 'measure']
	list_display = ('title', 'measure')
	list_filter = ['title', 'measure']
	search_fields = ['title']


admin.site.register(Product)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Attribute, AttributeAdmin)


admin.site.register(Attribute_measure)
admin.site.register(Attribute_title)
admin.site.register(Attribute_list)
