from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
#from .forms import *
from django import template

# Create your views here.

def display(request):
    return render(request, 'display.html',{'data_poultry': data.objects.all()})
