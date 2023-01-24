"""networks_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('ppr', views.ppr, name='ppr'),
    path('commands', views.commands, name='commands'),
    path('create', views.create, name='create'),
    path('about', views.about, name='about'),
    path('switches', views.switches, name='switches'),
    path('switches/<int:pk>', views.SwitchesDetailView.as_view(), name='switches-detail'),
    path('switches/<int:pk>/update', views.SwitchesUpdateView.as_view(), name='switches-update'),
    path('switches/<int:pk>/delete', views.SwitchesDeleteView.as_view(), name='switches-delete')
]
