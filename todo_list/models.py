from django.db import models
from django.contrib.auth.models import User
# time import??


# Create your models here.


# user is universal model
# user model basically a profile! login/sign up!
# todo model users can create a todo list, confirm if correct and makes a note of time created at.


class custom_user(models.Model):
    username = models.CharField(max_length=50, unique = True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(unique = True)
    # password = models.CharField(_('password'), max_length=128)
    is_staff = models.BooleanField(default = False)


    REQUIRED_FIELDS = ['username', 'firstname', 'lastname', 'email', 'password']


    class Meta:
        verbose_name = 'username'
        verbose_name_plural = 'usernames'
        ordering = ['email']

    def __str__(self):
        return self.email


class ToDo(models.Model):
    add_item = models.TextField(max_length=500)
    confirm = models.BooleanField(default = False)
    created_at = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
