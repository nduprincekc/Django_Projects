from django.shortcuts import render
from django.urls import path

# from elib.elib.urls import urlpatterns
from . import views

urlpatterns = [
    path('',views.index, name='index')

]
