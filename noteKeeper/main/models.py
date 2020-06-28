from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime
import django

class College(models.Model):
	college_name = models.CharField(max_length = 300)
	college_slug = models.CharField(max_length = 200, default = 1)

	class Meta:
		verbose_name_plural = "Colleges"

	def __str__(self):
		return self.college_name

class Department(models.Model):
	department_name = models.CharField(max_length = 200)
	college_name = models.ForeignKey(College, default = 1, verbose_name = "College", on_delete = models.SET_DEFAULT)
	department_slug = models.CharField(max_length = 200, default = 1)

	class Meta:
		verbose_name_plural = "Departments"

	def __str__(self):
		return self.department_name

class Semester(models.Model):
	sem = models.CharField(max_length = 20)
	department_name = models.ForeignKey(Department, default = 1, verbose_name = "Department", on_delete = models.SET_DEFAULT)
	sem_slug = models.CharField(max_length = 200, default = 1)

	class Meta:
		verbose_name_plural = "Semester"

	def __str__(self):
		return self.sem

class Subject(models.Model):
	sub_name = models.CharField(max_length = 200)
	department_name = models.ForeignKey(Department, default = 1, verbose_name = "Department", on_delete = models.SET_DEFAULT)
	sem = models.ForeignKey(Semester, default = 1, verbose_name = "Semester", on_delete = models.SET_DEFAULT)
	sub_slug = models.CharField(max_length = 200, default = 1)

	def __str__(self):
		return self.sub_slug

class Notes(models.Model):
	file_published = models.DateTimeField("date published", default = django.utils.timezone.now)
	file_pdf = models.FileField(upload_to = '')
	sub_slug = models.CharField(max_length = 120)

class Papers(models.Model):
	file_published = models.DateTimeField("date published", default = django.utils.timezone.now)
	file_pdf = models.FileField(upload_to = '')
	sem_slug = models.CharField(max_length = 120)

class UserProfile(models.Model):
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	city = models.CharField(max_length=100)
	country = models.CharField(max_length=100, default='India')

	def __str__(self):
		return self.first_name