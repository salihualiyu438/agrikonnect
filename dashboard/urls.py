from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('profile_photo', views.profile_photo, name='profile_photo')
]