from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, UserGroup, UserDetail
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(UserAdmin):
	add_form = UserCreationForm
	form = UserChangeForm
	model = User
	fieldsets = (
			(('Общие данные:'), {'fields': (('username', 'email'), 'password',)}),
			(('Дополнительно:'), {'fields': ('userpic',)}),
			(('Разрешения:'), {'fields': (('usergroup', 'is_admin', 'is_staff'),)}),
			(('Дополнительно:'), {'fields': ('details',)}),
			(('Служебная информация:'), {'fields': ('date_joined', 'last_login', 'slug')}),
		)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'email', 'password1', 'password2', 'slug')}
		),
	)

	list_display = ('username', 'email', 'usergroup', 'is_admin', 'is_staff', 'date_joined', 'last_login')
	search_fields = ('username', 'email',)
	readonly_fields = ('date_joined', 'last_login', 'slug',)
	ordering = ['-date_joined', ]

	filter_horizontal = ()
	list_filter = ()
admin.site.register(User, UserAdmin)


class UserGroupAdmin(admin.ModelAdmin):
	model = UserGroup
	fields = ('title', 'description',)
	list_display = ('title',)
	list_filter = ['title',]
	search_fields = ['title',]
admin.site.register(UserGroup, UserGroupAdmin)


class UserDetailAdmin(admin.ModelAdmin):
	model = UserDetail
	fieldsets = (
			(('ФИО:'), {'fields': (('name', 'surname', 'middle_name'),)}),
			(('Телефоны:'), {'fields': (('phone1','phone2'),)}),
			(('Общая информация:'), {'fields': (('city', 'company', 'position'),'comment',)}),
			(('Социальные сети:'), {'fields': (('watsapp', 'viber', 'telegram'), ('vk', 'facebook', 'twitter'), 'instagram',)}),
			(('Конфиденциальная информация:'), {'fields': ('card',)}),
		)

	list_display = ('name', 'surname', 'middle_name', 'company', 'position', 'city',)
	search_fields = ('name', 'surname', 'middle_name', 'company', 'city',)
	# readonly_fields = ('card',)
	# ordering = ['-date_joined', ]
admin.site.register(UserDetail, UserDetailAdmin)
