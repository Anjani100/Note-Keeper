from django.shortcuts import render
from .models import department


def homepage(request):
	return render(request = request,
				 template_name = "main/home.html",
				 context = {"department": department.objects.all})
