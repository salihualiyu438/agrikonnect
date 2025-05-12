from django.shortcuts import render
from .models import Notification
# Create your views here.

def notifications(request):
    
    return render(request, 'notifications.html')