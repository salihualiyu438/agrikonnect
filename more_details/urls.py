from django.urls import path
from . import views

urlpatterns=[
    path('plots/<pk>/', views.more_details, name='more_details'),
]