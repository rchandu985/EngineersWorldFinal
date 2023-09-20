from django.urls import path
from .views import fetch_qualifications_data

urlpatterns = [
    path('fetch_qualifications_data/',fetch_qualifications_data)
]
