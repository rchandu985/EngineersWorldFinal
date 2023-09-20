from django.urls import path
from Dashboard import views
urlpatterns = [
    path("auth/",views.validator),
]
