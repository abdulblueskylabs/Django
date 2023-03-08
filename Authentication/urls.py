from django.urls import path

from .views import login, sample_api

urlpatterns = [
    path('login', login),
    path('sampleapi', sample_api)

]