from django.shortcuts import render

def commands_home(request):
    return render(request, 'commands/commands_home.html')

def commands_work(request):
    return render(request, 'commands/commands_work.html')