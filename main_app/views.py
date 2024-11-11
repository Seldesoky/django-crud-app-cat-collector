from django.shortcuts import render
from .models import Cat

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Create your views here.

def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cat_index(request):
    # Render the cats/index.html template with the cats data
    cats = Cat.objects.all()  # look familiar?
    return render(request, 'cats/index.html', {'cats': cats})