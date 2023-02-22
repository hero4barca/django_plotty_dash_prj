from django.shortcuts import render
from django.http import HttpResponse
from plottyApp import plotty_apps, plotty_app2,  plotty_app3

# Create your views here.

def simple (request):
    return render (request, "plottyApp/home.html")

def scatter_graph (request):
    return render (request, "plottyApp/scatter_graph.html")

def product_bar (request):
    return render (request, "plottyApp/product_bar.html")
