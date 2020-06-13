from django.shortcuts import render, redirect
from .models import department, subject, year
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError


class UserEditView(generic.CreateView):
	form_class = UserChangeForm
	template_name = "main/profile.html"
	success_url = reverse_lazy("homepage")


def account(request, user):
	user = User.objects.get(username = username)
	return render(request,
				 template_name = "main/account.html",
				 context = {"user": user})

def homepage(request):
	return render(request = request,
				 template_name = "main/home.html",
				 context = {"department": department.objects.all})

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"New Account Created: {username}")
			login(request, user)
			messages.info(request, f"You are now logged in as {username}")
			return redirect("main:homepage")

		else:
			username = form.cleaned_data.get('username')
			password1 = form.cleaned_data.get('password1')
			password2 = form.cleaned_data.get('password2')
			print(form.cleaned_data)
			
			if not username:
				messages.error(request, f"Error: Username already exists")
			elif len(password1) < 8:
				messages.error(request, f"Error: Your password must be at least 8 digits long.")
			elif password1.isdigit():
				messages.error(request, f"Error: Your password cannot be fully numeric.")
			elif not (password1 and password2):
				messages.error(request, f"Error: {form.error_messages['password_mismatch']}")
			form = RegistrationForm()

			return render(request = request,
	                       template_name = "main/register.html",
	                       context={"form":form})

	form = RegistrationForm
	return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})


def logout_request(request):
	logout(request)
	messages.info(request, f"Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request = request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username = username, password = password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You logged in successfully in as {username}")
				return redirect('main:homepage')
			else:
				messages.error(request, f"Invalid username or password")
		else:
			messages.error(request, f"Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				 "main/login.html",
				 {"form":form})

