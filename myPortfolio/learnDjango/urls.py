from django.urls import path
from . import views

urlpatterns = [
    path('learnDjango', views.LearnDjango, name='learnDjango'),
]