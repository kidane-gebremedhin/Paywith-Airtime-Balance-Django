from django.db import models
from games.models import Game 
from price_type.models import PriceType 
from django.contrib.auth.models import User
from django.utils import timezone

class GamePrice(models.Model):
	game=models.ForeignKey(Game, on_delete=models.CASCADE)
	priceType=models.ForeignKey(PriceType, on_delete=models.CASCADE)
	priceInBirr=models.FloatField()
	created_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by_user')
	updated_by=models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True, editable=False, related_name='updated_by_user')
	created_at=models.DateTimeField(default=timezone.now, editable=False)
	updated_at=models.DateTimeField(default=None, blank=True, null=True, editable=False)

	def __str__(self):
		return f'{self.priceType.name} {self.priceInBirr} ---- Game: {self.game}'