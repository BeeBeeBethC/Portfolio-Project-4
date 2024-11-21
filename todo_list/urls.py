from . import views
from django.urls import path

urlpatterns = [
    path('', views.todolist.as_view(), name='home'),
]