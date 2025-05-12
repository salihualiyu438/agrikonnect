from django.shortcuts import render, get_object_or_404
from AgriKonnect.models import Plot

# Create your views here.

########   MORE DETAILS FUNCTION  ########
def more_details(request, pk):


    plots = get_object_or_404(Plot, pk=pk)
    return render(request, 'more_details.html', {'plots': plots})
