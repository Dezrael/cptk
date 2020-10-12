from django.shortcuts import render, redirect, reverse
# Сбиваем, дабы не путалась с нашим методом Login
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def login(request):
		context = {}
		if request.method == 'POST':
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(request, email=email, password=password)
			if user is not None:
				auth_login(request, user)
				return redirect(reverse("account:account"))
			else:
					context['error'] = "Логин или Пароль не совпадают"
		return render(request, 'account/login.html', context)


@login_required
def signout(request):
		logout(request)
		return render(request, 'account/login.html')


@login_required(login_url='account:login')
def account(request):
	return render(request, 'account/account.html')