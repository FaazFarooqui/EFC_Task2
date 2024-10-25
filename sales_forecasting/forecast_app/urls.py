# forecast_app/urls.py
from django.urls import path
from .views import forecast_view

urlpatterns = [
    path('forecast/', forecast_view, name='forecast'),
]