from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hola Come Home</h1>")

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")