from django.urls import path
from . import views

urlpatterns = [
    path('', views.commands_home, name='commands_home'),
    path('commands_work', views.commands_work, name='commands_work'),
]