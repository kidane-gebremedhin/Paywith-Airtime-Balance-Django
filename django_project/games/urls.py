from django.urls import path
from . import views
urlpatterns=[
path('upcoming_games/', views.upcoming_games, name='upcoming-games'),
]