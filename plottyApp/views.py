from django.shortcuts import render
from django.http import HttpResponse
from plottyApp import plotty_apps, plotty_app2, plotty_app3

# Create your views here.

def home (request):
    return render (request, "plottyApp/home.html")
