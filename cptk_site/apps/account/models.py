from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib import admin

from slugify import slugify


class AccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("Users must have email")
		if not username:
			raise ValueError("Users must have username")

		user = self.model(
			email=self.normalize_email(email).lower(),
			username=username,
		)

		user.set_password(password)
		user.save()
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email).lower(),
			username=username,
			password=password,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save()
		return user


class UserGroup(models.Model):
	title 				= models.CharField(verbose_name="Название группы", max_length=60, unique=True)
	description		= models.TextField(verbose_name="Описание группы", max_length=255)

	class Meta():
		verbose_name = "Группа пользователей"
		verbose_name_plural = "Группы пользователей"


class User(AbstractBaseUser):
	def profile_pic(instance, filename):
		ext = '.' + filename.split('.')[-1]
		path = "account/userprofiles/" + instance.slug + "/userpic/"
		format = instance.slug + ext
		return os.path.join(path, format)

	username			= models.CharField(verbose_name="Логин", max_length=30, unique=True)
	slug					= models.SlugField('URL', max_length=30, blank=False, unique=True)
	email					= models.EmailField(verbose_name="Почта", max_length=60, unique=True)
	password			= models.CharField(verbose_name="Пароль", max_length=100)
	userpic				= models.ImageField(verbose_name="Картинка профиля", upload_to=profile_pic, null=True, blank=True)
	usergroup			= models.ForeignKey(UserGroup, verbose_name='Группа', on_delete=models.CASCADE, null=True, blank=True)
	date_joined		= models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
	last_login		= models.DateTimeField(verbose_name="Дата последнего входа", auto_now=True)
	is_admin			= models.BooleanField(verbose_name="Админ.",default=False)
	is_active			= models.BooleanField(verbose_name="Активен",default=True)
	is_staff			= models.BooleanField(verbose_name="Персонал",default=False)
	is_superuser	= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [ 'username', ]

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.username)
		super().save(*args, **kwargs)

	objects = AccountManager()

	def def_userpic(self):
		if not self.image:
			return '/media/account/img/def_userpic.jpg'
		return self.image.url

	def __str__(self):
		return self.username

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

	class Meta():
			verbose_name = "Пользователь"
			verbose_name_plural = "Пользователи"

admin.site.register(User)