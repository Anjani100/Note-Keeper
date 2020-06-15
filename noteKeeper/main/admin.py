from django.contrib import admin
from .models import Department, Semester, Subject, College
from django.db import models

# Register your models here.

admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(College)
admin.site.register(Department)