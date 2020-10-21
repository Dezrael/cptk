from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe #For Showing Image-Miniatures

from .models import User, UserGroup, UserDetail
from .forms import UserCreationForm, UserChangeForm


class InLineDetails(admin.StackedInline):
	model = UserDetail
	extra = 0
	max_num = 1
	fieldsets = (
			((''), {'fields': (('name', 'surname', 'middle_name'),)}),
			(('Телефоны:'), {'fields': (('phone1','phone2'),)}),
			(('Общая информация:'), {'fields': (('city', 'company', 'position'),'comment',)}),
			(('Социальные сети:'), {'fields': (('watsapp', 'viber', 'telegram'), ('vk', 'instagram', 'twitter'),)}),
			(('Конфиденциальная информация:'), {'fields': ('card',)}),
		)


from django.utils.http import urlencode
class UserAdmin(UserAdmin):
	def preview(self, obj):
		if obj.userpic:
			return mark_safe('<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.userpic.url))
		else:
			return '(No image)'
	preview.short_description = "Превью:"

	# def showgroups(self, obj):
	# 	url = (
	# 		reverse("admin:core_person_changelist")
	# 		+ "?"
	# 		+ urlencode({"courses__id": f"{obj.id}"})
	# 	)
	# 	return format_html('<a href="{}">{} Students</a>', url, count)
	# 	view_students_link.short_description = "Students"


	inlines = [InLineDetails]
	add_form = UserCreationForm
	form = UserChangeForm
	model = User
	fieldsets = (
			(('Общие данные:'), {'fields': (('username', 'email'), 'password',)}),
			(('Дополнительно:'), {'fields': ('usergroup', ('userpic', 'preview',),)}),
			(('Разрешения:'), {'fields': (('groups', 'is_superuser', 'is_staff',),('user_permissions',))}),
			(('Служебная информация:'), {'fields': (('date_joined', 'last_login'), 'slug',)}),
		)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username','email', 'password1', 'password2', 'slug')},
		),
	)

	list_display = ('username', 'email', 'usergroup', 'is_superuser', 'is_staff', 'date_joined', 'last_login')
	search_fields = ('username', 'email',)
	readonly_fields = ('date_joined', 'last_login', 'slug', 'preview')
	ordering = ['-date_joined', ]

	filter_horizontal = ('user_permissions', )
	list_filter = ()

admin.site.register(User, UserAdmin)


class UserGroupAdmin(admin.ModelAdmin):
	model = UserGroup
	fieldsets = (
		(None, {
			'fields': ('title', 'description'),
			'description': "В описании необходимо кратко описать привилегии данного статуса."
		}),
	)
	list_display = ('title',)
admin.site.register(UserGroup, UserGroupAdmin)


class UserDetailAdmin(admin.ModelAdmin):
	model = UserDetail
	fieldsets = (
			(('Пользователь:'), {'fields': (('user',),)}),
			(('ФИО:'), {'fields': (('name', 'surname', 'middle_name'),)}),
			(('Телефоны:'), {'fields': (('phone1','phone2'),)}),
			(('Общая информация:'), {'fields': (('city', 'company', 'position'),'comment',)}),
			(('Социальные сети:'), {'fields': (('watsapp', 'viber', 'telegram'), ('vk', 'instagram', 'twitter'),)}),
			(('Конфиденциальная информация:'), {'fields': ('card',)}),
		)

	list_display = ('user', 'name', 'surname', 'middle_name', 'company', 'position', 'city',)
	search_fields = ('user','name', 'surname', 'middle_name', 'company', 'city',)
	list_filter = ('company', 'city','position',)
	readonly_fields = ('card',)
	# ordering = ['-date_joined', ]
admin.site.register(UserDetail, UserDetailAdmin)