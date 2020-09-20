from django.db import models
from games.models import Game 
from home_or_away_status.models import HomeOrAwayStatus 
from django.utils import timezone
from django.urls import reverse
import random, string

class PaymentRecord(models.Model):
	game=models.ForeignKey(Game, on_delete=models.CASCADE)
	ticketCode=models.CharField(default=None, blank=True, null=True, max_length=255)
	fullName=models.CharField(max_length=255)
	recipientAccountNumber=models.CharField(max_length=255)
	phoneNumber=models.CharField(max_length=255, null=True)
	paidAmount=models.FloatField()
	homeOrAwayStatus=models.ForeignKey(HomeOrAwayStatus, on_delete=models.CASCADE)
	date=models.DateTimeField(default=timezone.now)

	def save(self):
		auto_ticketCode=''
		old_records=PaymentRecord.objects
		if old_records.count() == 0:
			auto_ticketCode=self.generateTicketCode(5, uc=False, d=True)
		else:
			while old_records.count() > 0:
				auto_ticketCode=self.generateTicketCode(5, uc=False, d=True)
				#old_records=PaymentRecord.objects.filter(game=self.game).filter(ticketCode=auto_ticketCode)
				old_records=PaymentRecord.objects.filter(ticketCode=auto_ticketCode)
		
		self.ticketCode=auto_ticketCode
		super().save()

	def __str__(self):
		return f'{self.fullName} {self.phoneNumber} | Code: {self.ticketCode} | Payed: {self.paidAmount} Birr | To Account-No: {self.recipientAccountNumber}'

	def get_absolute_url(self):
		return reverse('send-ticket-code', args=[self.ticketCode, self.paidAmount])

	def generateTicketCode(request, str_len, uc=False, d=False):
		choices=string.ascii_lowercase
		if uc:
			choices+=string.ascii_uppercase
		if d:
			choices+=string.digits

		res="".join(random.choices(choices, k=str_len))
		return res