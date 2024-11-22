from django.shortcuts import render
from django.views import View
from .models import custom_user

# Create your views here.
class todolist(View):
    def get(self, request):
        return render(request, 'base.html')