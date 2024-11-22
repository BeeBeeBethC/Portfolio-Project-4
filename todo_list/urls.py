from . import views
from .views import todolist
from django.urls import path

urlpatterns = [
    path('', views.todolist.as_view(), name='home'),
]