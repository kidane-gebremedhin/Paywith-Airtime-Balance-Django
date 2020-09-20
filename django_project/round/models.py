from django.db import models
from django.utils import timezone
from competetion_type.models import CompetetionType

class Round(models.Model):
	name=models.CharField(unique=True, max_length=255)
	description=models.TextField(default=None, blank=True, null=True)
	CompetetionType=models.ForeignKey(CompetetionType, on_delete=models.CASCADE, null=True)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name+' - '+self.CompetetionType.name