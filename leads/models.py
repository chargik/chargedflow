from django.db import models

# Create your models here.
class Join(models.Model):
	name = models.CharField(max_length=128)
	telephone = models.CharField(max_length=15)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name