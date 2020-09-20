from django.db import models
from stadium.models import Stadium 
from competetion_type.models import CompetetionType 
from round.models import Round 
from club.models import Club
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse 
from django.urls import reverse

class Game(models.Model):
	stadium=models.ForeignKey(Stadium, on_delete=models.CASCADE)
	competetionType=models.ForeignKey(CompetetionType, on_delete=models.CASCADE)
	round=models.ForeignKey(Round, on_delete=models.CASCADE)
	homeSide=models.ForeignKey(Club, on_delete=models.CASCADE, related_name='home_side_club')
	awaySide=models.ForeignKey(Club, on_delete=models.CASCADE, related_name='away_side_club')
	game_dateTime=models.DateTimeField(default=timezone.now)
	created_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_created_by_user')
	updated_by=models.ForeignKey(User, on_delete=models.CASCADE, editable=False, default=None, blank=True, null=True, related_name='game_updated_by_user')
	created_at=models.DateTimeField(default=timezone.now, editable=False)
	updated_at=models.DateTimeField(default=None, blank=True, null=True, editable=False)

	def save(self):
		old_games=Game.objects.filter(competetionType=self.competetionType).filter(round=self.round).filter(homeSide=self.homeSide)
		if old_games.count()>0:
			if old_games.count() > 1 or old_games[0].id != self.id:
				print('Object duplicated')
				return HttpResponse('Object duplicated')
				
		super().save()

	def __str__(self):
		return f'{self.homeSide.name} Vs {self.awaySide.name} | {self.round.name}'

                
