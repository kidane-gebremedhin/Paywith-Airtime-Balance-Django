from django.db import models
from django.utils import timezone
from django.urls import reverse

class Record(models.Model):
	fullName=models.CharField(max_length=100)
	amount=models.CharField(max_length=100)
	date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.fullName

	def get_absolute_url(self):
		#return reverse('payment-detail', kwargs={'pk':self.pk})
		return reverse('send-post-response')

# class Stadium(models.Model):
# 	name=models.CharField(max_length=255)
# 	description=models.TextField()
# 	date=models.DateTimeField(default=timezone.now)

# class CompetetionType(models.Model):
# 	name=models.CharField(max_length=255)
# 	description=models.TextField()
# 	date=models.DateTimeField(default=timezone.now)

# class Round(models.Model):
# 	name=models.CharField(max_length=255)
# 	description=models.TextField()
#	competetionType=models.ForeignKey(CompetetionType, on_delete=models.CASCADE)
# 	date=models.DateTimeField(default=timezone.now)

# class Club(models.Model):
# 	name=models.CharField(max_length=255)
# 	description=models.TextField()
# 	date=models.DateTimeField(default=timezone.now)

# class GameStatus(models.Model):
# 	name=models.CharField(max_length=255)
# 	description=models.TextField()
# 	date=models.DateTimeField(default=timezone.now)

# class PriceType(models.Model):
# 	name=models.CharField(max_length=255)
# 	description=models.TextField()
# 	date=models.DateTimeField(default=timezone.now)

# class HomeOrAwayStatus(models.Model):
# 	name=models.CharField(max_length=255)
# 	description=models.TextField()
# 	date=models.DateTimeField(default=timezone.now)

# class Game(models.Model):
#	stadium=models.ForeignKey(Stadium, on_delete=models.CASCADE)
#	competetionType=models.ForeignKey(CompetetionType, on_delete=models.CASCADE)
#	round=models.ForeignKey(Round, on_delete=models.CASCADE)
#	homeSide=models.ForeignKey(Club, on_delete=models.CASCADE)
#	awaySide=models.ForeignKey(Club, on_delete=models.CASCADE)
# 	game_dateTime=models.DateTimeField()
# 	created_by=models.ForeignKey(User, on_delete=models.CASCADE)
# 	updated_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
# 	created_at=models.DateTimeField(default=timezone.now)
# 	updated_at=models.DateTimeField(null=TRUE)

# class GamePrice(models.Model):
#	game=models.ForeignKey(Game, on_delete=models.CASCADE)
#	priceType=models.ForeignKey(PriceType, on_delete=models.CASCADE)
#	priceInBirr=models.DoubleField()
# 	created_by=models.ForeignKey(User, on_delete=models.CASCADE)
# 	updated_by=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
# 	created_at=models.DateTimeField(default=timezone.now)
# 	updated_at=models.DateTimeField(null=TRUE)

# class PaymentRecord(models.Model):
#	game=models.ForeignKey(Game, on_delete=models.CASCADE)
#	ticketCode=models.CharField(max_length=255)
#	fullName=models.CharField(max_length=255)
#	phoneNumber=models.CharField(max_length=255)
#	paidAmount=models.DoubleField()
# 	homeOrAwayStatus=models.ForeignKey(HomeOrAwayStatus, on_delete=models.CASCADE)

#-----MAIN TABLES---
# Game: { stadiumId, competetionTypeId, roundId, homeSideId, awaySideId, game_dateTime, created_by, updated_by, created_at, updated_at}
# GamePrice: { gameId, priceTypeId, priceInBirr, created_by, updated_by, created_at, updated_at}
# PaymentRecord: {gameId, ticketCode, fullName, phoneNumber, paidAmount, homeOrAwayStatus}
#-----META DATA----
# stadium:{name, description}
# competetionType:{name, description}
# round:{competetionTypeId, name, description}
# club:{name, description}
# gameStatus:{name, description}
# priceType:{name, description}
# homeOrAwayStatus:{name, description}
