from django.shortcuts import render
#from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def remoiseli(request):
    return render(request, 'remoiseli.html')    