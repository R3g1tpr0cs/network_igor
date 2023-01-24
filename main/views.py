from django.shortcuts import render
from django.http import request
from .forms import SwitchesForm
from .models import Switches
from django.views.generic import DetailView, UpdateView, DeleteView

def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', data,)

def ppr(request):
    return render(request, 'ppr/ppr_home.html')

def commands(request):
    return render(request, 'commands/commands_home.html')

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = SwitchesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'
    
    form = SwitchesForm()
    
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'main/create.html', data)

def switches(request):
    equipment = Switches.objects.order_by('location')
    return render(request, 'main/switches.html', {'equipment': equipment})

class SwitchesDetailView(DetailView):
    model = Switches
    template_name = 'main/details_view.html'
    context_object_name = 'switch'
    
class SwitchesUpdateView(UpdateView):
    model = Switches
    template_name = 'main/create.html'
    form_class = SwitchesForm
    
class SwitchesDeleteView(DeleteView):
    model = Switches
    success_url = '/switches'
    template_name = 'main/switches_delete.html'

