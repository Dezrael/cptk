from django.contrib import admin

# Register your models here.
from .models import Manufacturer, Category, Product, Attribute, Attribute_measure, Attribute_list, Attribute_title

class ManufacturerAdmin(admin.ModelAdmin):
	fields = ['title', 'image', 'description', 'link']
	list_display = ('title', 'link', 'slug')
	list_filter = ['title']
	search_fields = ['title']
	# prepopulated_fields = {"slug": ("title",)}



from .forms import CategoryForm
from mptt.admin import MPTTModelAdmin
from django.utils.safestring import mark_safe #For Showing Image-Miniatures

class CategoryAdmin(MPTTModelAdmin):
	form = CategoryForm

	def preview(self, obj):
		if obj.img:
			return mark_safe('<img src="{0}" width="100" height="100" style="object-fit:contain" />'.format(obj.img.url))
		else:
			return '(No image)'
	preview.short_description = "Превью"

	def have_descr(self, obj):
		return obj.description != ""
	have_descr.boolean = True
	have_descr.short_description = "Описание"

	def have_img(self, obj):
		return obj.img != ""
	have_img.boolean = True
	have_img.short_description = "Картинка"

	def have_svg(self, obj):
		return obj.svg != ""
	have_svg.boolean = True
	have_svg.short_description = "SVG"

	model = Category
	fieldsets = (
			(('Общие данные:'), {'fields': (('title', 'parent', 'hidden'),)}),
			(('Дополнительно:'), {'fields': ('description', ('svg', 'img', 'preview',),('attr_list', 'selectable_attr_list',),)}),
			(('Служебная информация:'), {'fields': ('slug', 'add_date',)}),
		)

	list_display = ('title', 'parent', 'hidden', 'have_descr', 'have_img', 'have_svg')
	search_fields = ['title']
	readonly_fields = ['add_date', 'slug', 'preview',]
admin.site.register(Category, CategoryAdmin)


class AttributeAdmin(admin.ModelAdmin):
	def slug(self, obj):
		return "{0} - {1}".format(obj.title, obj.measure)
	slug.short_description = "Характеристика"

	fields = ['title', 'measure']
	list_display = ('slug','title', 'measure')
	list_filter = ['title', 'measure',]
	search_fields = ['title']
	# list_editable = ['measure','title']
	list_display_links = ['slug']



admin.site.register(Product)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Attribute, AttributeAdmin)


admin.site.register(Attribute_measure)
admin.site.register(Attribute_title)
admin.site.register(Attribute_list)


from .models import Orders, ProductImages, ProductFiles, SelectableAttribute, SelectableAttribute_list, AtrributeChoises
admin.site.register(Orders)
admin.site.register(ProductImages)
admin.site.register(ProductFiles)

admin.site.register(SelectableAttribute)
admin.site.register(SelectableAttribute_list)
admin.site.register(AtrributeChoises)