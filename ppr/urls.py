from django.urls import path
from . import views

urlpatterns = [
    path('', views.ppr_home, name='ppr_home'),
    path('ppr_work', views.ppr_work, name='ppr_work'),
]
