from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserChangeForm, UserCreationForm

from .models import User


class UserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'slug')
		prepopulated_fields = {"slug": ("username",)}


class UserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField(label=("Password"),
        help_text=("Показывать вам пароль здесь - было бы не красиво, используйте <a href=\"../password/\">эту форму</a> для смены пароля."))
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'userpic', 'usergroup', 'is_staff', 'is_admin', 'slug')

    def clean_password(self):
        return self.initial["password"]


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {'email', 'password',}

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)