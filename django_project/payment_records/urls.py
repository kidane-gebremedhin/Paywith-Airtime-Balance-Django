from django.urls import path
from .views import PaymentCreateView, PaymentListView, PaymentDetailView, send_ticket_code, search_by_name, search_by_ticketCode, search_by_phone

urlpatterns=[
	path('create_payment/', PaymentCreateView.as_view(), name='submit-payment'),
	path('', PaymentListView.as_view(), name='list-payment-records'),
	path('detail/<int:pk>', PaymentDetailView.as_view(), name='payment-records-detail'),
	path('search_by_name/', search_by_name, name='search-by-name'),
	path('search_by_phone/', search_by_phone, name='search-by-phone'),
	path('search_by_ticketCode/', search_by_ticketCode, name='search-by-ticketCode'),
    path('send_ticket_code/<ticketCode>/<paidAmount>', send_ticket_code, name='send-ticket-code'),
]