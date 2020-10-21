from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group

from .models import User, UserGroup


class UserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = User
		fields = ('username', 'email', 'password1', 'password2')


class UserChangeForm(UserChangeForm):
	password 	= ReadOnlyPasswordHashField(
		label=("Пароль"),
		help_text=("Показывать вам пароль здесь - было бы не красиво, используйте <b><a href=\"../password/\">эту форму</a></b> для смены пароля.")
	),
	username 	= forms.CharField(
		label=("Логин:"),
		required=False,
	),
	groups 		= forms.ModelMultipleChoiceField(
		queryset=Group.objects.all(),
		label=("Группа:"),
		help_text=("Для выбора нескольких используйте <b>CTRL</b>."),
		required=False,
	)
	usergroup	= forms.ModelChoiceField(
		queryset=UserGroup.objects.all(),
		label=("Статус:"),
		help_text=("Изменяется в зависемости от статуса клиента в компании."),
		required=False,
	)
	class Meta:
		model = User
		fields = ('username', 'email', 'password', 'userpic', 'usergroup', 'is_staff', 'slug')

	def clean_password(self):
		return self.initial["password"]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'email', 'password',}

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)