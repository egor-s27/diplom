from django.urls import path
from . import views

# Отследивание URL адресов
urlpatterns = [
    path('', views.index, name='home'),
    path('bz', views.baza, name='bz')
]