from django.db import models


class department(models.Model):
	department_name = models.CharField(max_length = 200)
	department_slug = models.CharField(max_length = 200, default = 1)

	def __str__(self):
		return self.department_name
