from django.core.validators import FileExtensionValidator, MinValueValidator
from django.utils import timezone
import datetime, os
from django.contrib import admin
import uuid
from django.shortcuts import reverse

from slugify import slugify

from django.db import models

class Manufacturer(models.Model):
	def manufact_pic(instance, filename):
		ext = '.' + filename.split('.')[-1]
		path = "catalog/manufacturer/" + instance.slug
		format = instance.slug + ext
		return os.path.join(path, format)

	title = models.CharField(verbose_name="Название компании", max_length=60, unique=True)
	slug = models.SlugField(verbose_name="URL", unique=True)
	image = models.FileField(verbose_name="Логотип", upload_to=manufact_pic, validators=[FileExtensionValidator(['svg', 'png', 'jpg', 'jpeg', 'webp'])], blank=True)
	description	= models.TextField(verbose_name="Описание", max_length=1500, blank=True)
	link = models.CharField(verbose_name="Ссылка на сайт", max_length=120, blank=True)

	def save(self):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Manufacturer, self).save()

	def __str__(self):
		return self.title

	class Meta():
		db_table = 'manufacturer'
		verbose_name = "(3) Производитель"
		verbose_name_plural = "(3) Производители"


class Attribute_title(models.Model):
	title = models.CharField(verbose_name="Наименование атрибута", max_length=60, unique=True)
	class Meta():
		verbose_name = "Наименование атрибута"
		verbose_name_plural = "Наименование атрибутов"
	def __str__(self):
		return self.title

class Attribute_measure(models.Model):
	measure	= models.CharField(verbose_name="Значение", max_length=60, unique=True)
	class Meta():
		verbose_name = "Единица измерения"
		verbose_name_plural = "Единицы измерения"
	def __str__(self):
		return self.measure

class Attribute(models.Model):
	title = models.ForeignKey(Attribute_title, verbose_name='Атрибут', on_delete=models.CASCADE)
	measure	= models.ForeignKey(Attribute_measure, verbose_name='Ед. Измерения', on_delete=models.CASCADE)
	def __str__(self):
		return self.title.title + ' - ' + self.measure.measure

	class Meta():
		verbose_name = "(4) Атрибут"
		verbose_name_plural = "(4) Атрибуты"


class AtrributeChoises(models.Model):
	choise = models.CharField(verbose_name='Вариант', max_length=120, unique=True)
	class Meta():
		verbose_name = "Вариант атрибутов"
		verbose_name_plural = "Варианты атрибутов"
	def __str__(self):
		return self.choise

class SelectableAttribute(models.Model):
	title = models.CharField(verbose_name='Наименование', max_length=120, unique=True)
	choises	= models.ManyToManyField(AtrributeChoises, verbose_name='Варианты')
	def __str__(self):
		return self.title

	class Meta():
		verbose_name = "(5) Выбираемый атрибут"
		verbose_name_plural = "(5) Выбираемые атрибуты"

class Category(models.Model):
	def category_pic(instance, filename):
		ext = '.' + filename.split('.')[-1]
		path = "catalog/category/pics/" + instance.slug
		format = instance.slug + ext
		return os.path.join(path, format)

	title = models.CharField(verbose_name="Наименование:", max_length=90, unique=True)
	slug = models.SlugField(verbose_name="URL:", max_length=90, unique=True)
	parent = models.ForeignKey("self", verbose_name="Категория родитель:",on_delete=models.CASCADE, blank=True, null=True)
	description = models.TextField(verbose_name="Описание категории", max_length=1500, blank=True,)
	svg	= models.CharField(verbose_name="Название SVG, для меню", max_length=30, blank=True,)
	img	= models.ImageField(verbose_name="Изображение для категории", upload_to=category_pic, blank=True)
	attr_list = models.ManyToManyField(Attribute, verbose_name="Атрибуты для категории", blank=True)
	selectable_attr_list = models.ManyToManyField(SelectableAttribute, verbose_name="Выбираемые атрибуты для категории", blank=True)

	def save(self):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Category, self).save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('category',kwargs={'slug': self.slug})

	class Meta():
		db_table = 'category'
		verbose_name = "(2) Категория"
		verbose_name_plural = "(2) Категории"


class Product(models.Model):
	def get_file_path(instance, filename):
		path = "catalog/" + instance.slug + "/images/"
		return os.path.join(path, filename)

	title = models.CharField(verbose_name='Наименование', max_length=120, unique=True)
	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
	manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.CASCADE)
	articul	= models.IntegerField(verbose_name="Артикул")
	slug = models.SlugField(verbose_name='URL', max_length=30, blank=False, unique=True)
	img	= models.ImageField(verbose_name='Главная картинка', upload_to=get_file_path)
	price = models.DecimalField(('Цена за 1'), decimal_places=2,max_digits=12, default=1.00, validators=[MinValueValidator(1.0)],)
	s_description = models.TextField(verbose_name="Краткое описание", max_length=600)
	description	= models.TextField(verbose_name="Полное описание", max_length=2000)
	add_date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)

	def get_absolute_url(self):
		return reverse('product',kwargs={'slug': self.slug})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		if self.articul is None:
			self.articul = 0
			super(Product, self).save()
			s_category = '{:02}'.format(self.category.id)
			s_manufacturer = '{:03}'.format(self.manufacturer.id)
			s_id = '{:03}'.format(self.id)
			self.articul = int('{category}{manufacturer}{id}'.format(category=s_category, manufacturer = s_manufacturer, id = s_id))
		super(Product, self).save()


	def __str__(self):
		return self.title

	class Meta():
		db_table = 'product'
		verbose_name = "(1) Товар"
		verbose_name_plural = "(1) Товары"

class ProductImages(models.Model):
	def get_file_path(instance, filename):
		path = "catalog/" + instance.product.slug + "/images/"
		return os.path.join(path, filename)

	product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
	image = models.ImageField(verbose_name='Изображение', upload_to=get_file_path)

	def __str__(self):
		return self.product.title + ' - ' + str(self.id)

	class Meta():
		verbose_name = "Изображения товаров"
		verbose_name_plural = "Изображения товаров"

class ProductFiles(models.Model):
	def get_file_path(instance, filename):
		path = "catalog/" + instance.product.slug + "/files/"
		return os.path.join(path, filename)

	title = models.CharField(verbose_name='Наименование', max_length=120)
	product = models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
	file = models.FileField(verbose_name='Файл', upload_to=get_file_path)

	def __str__(self):
		return self.product.title + ' - ' + self.title

	class Meta():
		verbose_name = "Файлы товаров"
		verbose_name_plural = "Файлы товаров"

class Attribute_list(models.Model):
	product	= models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
	attribute = models.ForeignKey(Attribute, verbose_name='Атрибут', on_delete=models.CASCADE)
	value = models.CharField(verbose_name='Значение', max_length=20)

	def __str__(self):
		return '{product} - {attribute}'.format(product = self.product.title, attribute = self.attribute.title.title)

	class Meta():
		verbose_name = "Пул атрибутов"
		verbose_name_plural = "Пул атрибутов"


class SelectableAttribute_list(models.Model):
	product	= models.ForeignKey(Product, verbose_name='Товар', on_delete=models.CASCADE)
	attribute = models.ForeignKey(SelectableAttribute, verbose_name='Атрибут', on_delete=models.CASCADE)
	value = models.ForeignKey(AtrributeChoises, verbose_name='Значение', on_delete=models.CASCADE)

	def __str__(self):
		return '{product} - {attribute}'.format(product = self.product.title, attribute = self.attribute.title)

	class Meta():
		verbose_name = "Пул выбираемых атрибутов"
		verbose_name_plural = "Пул выбираемых атрибутов"

ORDER_STATUS_CHOICES = (
    ('Оформлен', 'Оформлен'),
		('В обработке', 'В обработке'),
    ('Готов', 'Готов')
)

class Orders(models.Model):
	first_name = models.CharField(max_length = 120, verbose_name = "Имя")
	last_name = models.CharField(max_length = 120, db_index=True, verbose_name = "Фамилия")
	email = models.CharField(max_length = 120, verbose_name = "E-mail")
	address = models.CharField(max_length = 120, verbose_name = "Адрес")
	comment = models.TextField(verbose_name = "Комментарий")
	products = models.TextField(verbose_name = "Товары")
	status = models.CharField(default= 'Оформлен', max_length=100, choices=ORDER_STATUS_CHOICES)
	total_price = models.DecimalField(max_digits=100, decimal_places=2, verbose_name = "Итоговая стоимость", default=0.00)

	def __str__(self):
		return "#{0} - {1} {2}".format(self.id, self.last_name, self.first_name)

	class Meta:
		verbose_name = "(6) Заказ"
		verbose_name_plural = "(6) Заказы"

admin.site.register(Orders)
admin.site.register(ProductImages)
admin.site.register(ProductFiles)

admin.site.register(SelectableAttribute)
admin.site.register(SelectableAttribute_list)
admin.site.register(AtrributeChoises)