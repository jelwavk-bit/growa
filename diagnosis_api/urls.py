from django.urls import path
from django.urls import path
from .views import PredictDisease

urlpatterns = [
    # Full URL: http://127.0.0.1:8000/api/diagnose/
    path('diagnose/', PredictDisease.as_view(), name='predict_disease'),
]