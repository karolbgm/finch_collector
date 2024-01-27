from django.urls import path
from . import views

urlpatterns = [
# Define all the app level urls in this list
    path('', views.home, name='home'),
]
