from django.db import models

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
	sem_slug = models.CharField(max_length = 200, default = 1)

	class Meta:
		verbose_name_plural = "Semester"

	def __str__(self):
		return self.sem

class Subject(models.Model):
	sub_name = models.CharField(max_length = 200)
	department_name = models.ForeignKey(Department, default = 1, verbose_name = "Department", on_delete = models.SET_DEFAULT)
	sub_file = models.CharField(max_length = 200)
	sem = models.ForeignKey(Semester, default = 1, verbose_name = "Semester", on_delete = models.SET_DEFAULT)
	sub_slug = models.CharField(max_length = 200, default = 1)

	def __str__(self):
		return self.sub_name
