from django.shortcuts import render
from .models import Plot

# Create your views here.

def home(request):

    plots = Plot.objects.all()
    return render(request, 'index.html', {'plots': plots})

