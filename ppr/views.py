from django.shortcuts import render
from main.models import Switches

def ppr_home(request):
    return render(request, 'ppr/ppr_home.html')

def ppr_work(request):
    equipment = Switches.objects.order_by('location')
    return render(request, 'ppr/ppr_work.html', {'equipment': equipment})