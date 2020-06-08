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
