from django.shortcuts import render, redirect
from .models import department, subject, year
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
from django.http import HttpResponse

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
            for msg in form.error_messages:
            	messages.error(request, f"{msg}: {form.error_messages[msg]}")

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
				return redirect('/')
			else:
				messages.info(request, f"Invalid username or password")
	else:
		messages.info(request, f"Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				 "main/login.html",
				 {"form":form})
def account_page(request):
	return render(request,
				 "main/account.html",
				 )






