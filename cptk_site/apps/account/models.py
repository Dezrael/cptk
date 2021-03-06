from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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
		verbose_name 				= "Статус"
		verbose_name_plural = "Статусы"

	def __str__(self):
		return self.title


class UserDetail(models.Model):
	name				= models.CharField(verbose_name="Имя:", max_length=32, blank=True)
	surname			= models.CharField(verbose_name="Фамилия:", max_length=32, blank=True)
	middle_name	= models.CharField(verbose_name="Отчество:", max_length=32, blank=True)
	phone1			= models.CharField(verbose_name="Телефон", max_length=16, blank=True, unique=True)
	phone2			= models.CharField(verbose_name="Телефон доп.", max_length=16, blank=True, unique=True)
	city				= models.CharField(verbose_name="Город:", max_length=32, blank=True)
	company			= models.CharField(verbose_name="Компания:", max_length=64, blank=True)
	position		= models.CharField(verbose_name="Должность:", max_length=32, blank=True)
	comment			= models.TextField(verbose_name="Комментарий:", max_length=16, blank=True)
	card				= models.CharField(verbose_name="Номер Карты:", max_length=16, blank=True, unique=True)
	watsapp			= models.CharField(verbose_name="WatsApp:", max_length=32, blank=True)
	viber				= models.CharField(verbose_name="Viber:", max_length=32, blank=True)
	vk					= models.CharField(verbose_name="ВК:", max_length=32, blank=True)
	facebook		= models.CharField(verbose_name="FaceBook:", max_length=32, blank=True)
	twitter			= models.CharField(verbose_name="Twitter:", max_length=32, blank=True)
	telegram		= models.CharField(verbose_name="Telegram:", max_length=64, blank=True)
	instagram		= models.CharField(verbose_name="Instagram:", max_length=64, blank=True)
	class Meta():
			verbose_name 				= "Доп. Информация пользователя"
			verbose_name_plural = "Доп. Информация пользователя"
	def __str__(self):
		return self.name + ' ' + self.surname + ' ' + self.middle_name


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
	details				= models.OneToOneField(UserDetail, verbose_name='Детали', on_delete=models.CASCADE, null=True, blank=True)

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




# Класс модели для хранения настроек пользователя (1 - скрыть информацию профиля)
# class UserSettings(models.Model):
# 	visability= models.BooleanField(verbose_name="Видемость:", default=True)


# Избранные товары/услуги пользователя
# 	class UserFavorite(models.Model):
# 		fav_id 		Id понравившегося товара/услуги
# 		add_date	Дата добавления в избранное