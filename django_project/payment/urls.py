from django.urls import path
from .views import RecordCreateView, RecordDetailView
from . import views

urlpatterns=[
	path('create/', RecordCreateView.as_view(), name='payment-create'),
	path('detail/<int:pk>', RecordDetailView.as_view(), name='payment-detail'),
]