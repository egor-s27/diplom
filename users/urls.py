from django.urls import path
from . import views

# Отследивание URL адресов
urlpatterns = [
    path('', views.login, name='login'),
    path('vhod', views.login_view, name='vhod'),
    path('home', views.user_home, name='user_home'),
    path('<int:pk>', views.UserDetailView.as_view(), name='user-detail')
]