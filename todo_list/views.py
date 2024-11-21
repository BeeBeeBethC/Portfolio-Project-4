from django.shortcuts import render
from django.views import generic
from .models import custom_user

# Create your views here.
class todolist(generic.ListView):
    model = custom_user