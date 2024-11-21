from . import views
from django.urls import path

urlpatterns = [
    path('', views.custom_user.as_view(), name='home'),
]