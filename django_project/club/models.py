from django.db import models
from django.utils import timezone

class Club(models.Model):
	name=models.CharField(unique=True, max_length=255)
	accountNumber=models.CharField(max_length=255)
	description=models.TextField(default=None, blank=True, null=True)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name
