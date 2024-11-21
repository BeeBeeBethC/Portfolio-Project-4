from django.shortcuts import render
from django.views.generic import ListView
from .models import custom_user

# Create your views here.
class todolist(ListView):
    model = custom_user