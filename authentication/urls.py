from django.urls import path
from .views import (
    CustomPasswordResetConfirmView,
    CustomPasswordResetView,
    PasswordResetDoneView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]