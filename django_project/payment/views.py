from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from payment.models import Record
from django.urls import reverse
from django.http import JsonResponse, HttpResponse

from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class RecordCreateView(CreateView):
	model=Record
	fields=['fullName', 'amount']

	# @method_decorator(csrf_exempt)
	# def dispatch(self, request, *args, **kwargs):
	# 	return HttpResponse('haha')

	# def get_success_url(self):
	# 	return reverse('payment-detail', kwargs={'pk':self.object.pk})
	
	# def get(self, request, *args, **kwargs):
	#     return HttpResponse('Ha!')

	# def post(self, request, *args, **kwargs):
	#     return HttpResponse('Ha!')

class RecordDetailView(DetailView):
	model=Record

	# # Simplly Comment this out to work as usual
	# def get(self, request, *args, **kwargs):
	# 	data = {
 #        'name': 'Vitor',
 #        'location': 'Finland',
 #        'is_active': True,
 #        'count': 28
 #    	}
	# 	return JsonResponse(data)


	
