from django.contrib import admin
from .models import department, year, subject, college
from django.db import models

# Register your models here.
class departmentAdmin(admin.ModelAdmin):
	fieldsets = [
		('Subject Name', {'fields': ['sub_name']}),
		("URL", {'fields': ["sub_slug"]}),
		("Year", {'fields': ["sub_year"]}),
		('Notes', {'fields': ['sub_file']})
	]

admin.site.register(subject)
admin.site.register(year)
admin.site.register(college)

admin.site.register(department, departmentAdmin)