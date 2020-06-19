from django.shortcuts import render, redirect
from .models import Department, Subject, Semester, College, UserProfile, Notes
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, UserProfileForm, NotesForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect


def edit_user(request):
	return render(request = request,
                  template_name = "main/profile.html",
                  context = {"userpro": UserProfile.objects.all})

def homepage(request):
	return render(request = request,
				 template_name = "main/home.html",
				 context = {"department": Department.objects.all})

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
				messages.info(request, f"You are now logged in as {username}")
				return redirect('main:homepage')
			else:
				messages.error(request, f"Invalid username or password")
		else:
			messages.error(request, f"Invalid username or password")

	form = AuthenticationForm()
	return render(request,
				 "main/login.html",
				 {"form":form})

def college(request):
	return render(request,
				  "main/college.html",
				  {"colleges": College.objects.all})

def department(request):
	return render(request,
				  "main/department.html",
				  {"department": Department.objects.all})

def single_slug(request, single_slug):

	department = [d.department_slug for d in Department.objects.all()]

	if single_slug in department:
		matching_series = Semester.objects.filter(department_name__department_slug = single_slug)
		sem_urls = {}

		for m in matching_series.all():
			part_one = m.sem_slug
			sem_urls[m] = part_one

		return render(request = request,
					  template_name = "main/semester.html",
					  context = {"semester": matching_series, "part_ones": sem_urls})

	semester = [s.sem_slug for s in Semester.objects.all()]

	if single_slug in semester:
		matching_series = Subject.objects.filter(sem__sem_slug = single_slug)
		sub_urls = {}

		for m in matching_series.all():
			part_one = m.sub_slug
			sub_urls[m] = part_one

		return render(request = request,
					  template_name = "main/subject.html",
					  context = {"subject": matching_series, "part_ones": sub_urls})

	subject = [s.sub_slug for s in Subject.objects.all()]

	if single_slug in subject:

		if request.method == 'POST':
			for f in request.FILES.getlist('file_pdf'):
				form = NotesForm(request.POST, request.FILES)
				if form.is_valid():
					obj = form.save(commit=False)
					obj.file_pdf = f
					form.save()
			s = "/notes/" + single_slug + "/notes-list"
			return redirect(s)

		else:
			form = NotesForm()
		return render(request = request,
					  template_name = 'main/files.html',
					  context = {"form": form, "slug": single_slug})

	else:
		return HttpResponse("<p>Error 404: Page Not Found!</p>")

def notes_list(request, slug):
	slugs = {}
	slugs['slug'] = slug
	return render(request = request,
				  template_name = "main/notes_list.html",
				  context = {"notes": Notes.objects.all, "slugs": slugs})

def delete_notes(request, slug, pk):
	if request.method == 'POST':
		note = Notes.objects.get(pk = pk)
		note.delete()
	return redirect("main:homepage")

def info(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("main:profile")
	else:
		form = UserProfileForm()
		return render(request = request,
				  	template_name = "main/info.html",
				  	context = {"form": form})