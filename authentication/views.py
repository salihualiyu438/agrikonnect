from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from .forms import CustomPasswordResetForm
from django.views.generic import TemplateView


class CustomPasswordResetView(PasswordResetView):
    form_class= CustomPasswordResetForm
    template_name = 'password_reset_form.html'
    success_url = '/authentication/password_reset_done/'


class PasswordResetDoneView(TemplateView):
    template_name = 'password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'password_reset_confirm.html'
    success_url = '/authentication/password_reset_complete/'


class PasswordResetCompleteView(TemplateView):
    template_name = 'password_reset_complete.html'