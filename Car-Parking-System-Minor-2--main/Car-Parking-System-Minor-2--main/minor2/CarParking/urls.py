from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('cps', views.cps),
]