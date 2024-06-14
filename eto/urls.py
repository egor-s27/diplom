from django.urls import path
from . import views

# Отследивание URL адресов
urlpatterns = [
    path('', views.eto_home),
    path('add', views.add, name='add'),
    path('<int:pk>', views.EtoDetailView.as_view(), name='eto-detail'), #отслеживаем динамический параметр
    path('<int:pk>/update', views.EtoUpdateView.as_view(), name='eto-update'),
    path('<int:pk>/delete', views.EtoDeleteView.as_view(), name='eto-delete')
]