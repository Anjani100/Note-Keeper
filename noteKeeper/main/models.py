from django.db import models

class department(models.Model):
	department_name = models.CharField(max_length = 200)
	department_slug = models.CharField(max_length = 200, default = 1)

	def __str__(self):
		return self.department_name

class year(models.Model):
	year = models.CharField(max_length = 20)
	department_name = models.CharField(max_length = 200)
	year_slug = models.CharField(max_length = 200, default = 1)

	def __str__(self):
		return self.year

class subject(models.Model):
	sub_name = models.CharField(max_length = 200)
	sub_file = models.CharField(max_length = 200)
	sub_year = models.CharField(max_length = 20)
	sub_slug = models.CharField(max_length = 200, default = 1)

	def __str__(self):
		return self.sub_name

class college(models.Model):
	college_name = models.CharField(max_length = 300)
	department_name = models.CharField(max_length = 200)
	college_slug = models.CharField(max_length = 200, default = 1)

	def __str__(self):
		return self.college_name