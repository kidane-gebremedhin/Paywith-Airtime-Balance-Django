from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView
from django.http import JsonResponse 
from django.shortcuts import render
from django.urls import reverse
from .models import PaymentRecord
import re, random, string

class PaymentCreateView(CreateView):
	model=PaymentRecord
	fields=['game', 'ticketCode', 'fullName', 'phoneNumber', 'paidAmount', 'homeOrAwayStatus', 'recipientAccountNumber']

	def dispatch(self, request, *args, **kwargs):
		# if self.mobile(self.request) or self.request.method=='GET':
		# 	print(self.request.META['HTTP_USER_AGENT'])
		# 	print('Bad Request Forbidden')
		# 	return render(self.request, 'payment_records/bad_request.html')
		return super(PaymentCreateView, self).dispatch(request, *args, **kwargs)

	def mobile(default_request,request):
		MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)", re.IGNORECASE)
		if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
			return True
		else:
			return False

class PaymentListView(ListView):
	model=PaymentRecord
	context_object_name='objects'
	ordering=['-date']

class PaymentDetailView(DetailView):
	model=PaymentRecord

def search_by_name(request):
	pattern=''
	if request.method=='POST':
		pattern=request.POST['fullName']

	objects=PaymentRecord.objects.filter(fullName__contains=pattern)
	return render(request, 'payment_records/search_result.html', {'objects':objects})

def search_by_phone(request):
	pattern=''
	if request.method=='POST':
		pattern=request.POST['phoneNumber']

	objects=PaymentRecord.objects.filter(phoneNumber__contains=pattern)
	return render(request, 'payment_records/search_result.html', {'objects':objects})

def search_by_ticketCode(request):
	pattern=''
	if request.method=='POST':
		pattern=request.POST['ticketCode']

	objects=PaymentRecord.objects.filter(ticketCode=pattern)
	return render(request, 'payment_records/ticket_verification_result.html', {'objects':objects})

def send_ticket_code(request, ticketCode, paidAmount):
	return JsonResponse({'type':'notification', 'success':True, 'ticketCode':ticketCode, 'paidAmount':paidAmount})