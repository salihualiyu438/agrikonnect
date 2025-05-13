from django.shortcuts import render, redirect
from .forms import UserProfileForm
from notifications.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def dashboard(request):
    if User.is_authenticated:
        return render(request, 'dashboard.html')
    else:
        return redirect('/')
@login_required
def profile_photo(request):
    if request == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('dashboard')
    else:
        try:
            profile = UserProfile.objects.get(user=request.user)
            form = UserProfileForm(instance=profile)
        except:
            form = UserProfileForm()
        
    return render(request, 'profile_photo.html', {'form': form})