from django.shortcuts import render

# Create your views here.

def terms_of_service(request):

    return render(request, 'terms_of_service.html')