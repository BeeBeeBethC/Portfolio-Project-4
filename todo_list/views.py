from django.shortcuts import render
from django.views.generic import ListView
from .models import custom_user

# Create your views here.
class todolist(ListView):
    queryset = custom_user.objects.all()
    template_name = "base.html"