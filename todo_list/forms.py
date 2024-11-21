from django import forms
from .models import custom_user, ToDo

class userForm(forms.ModelForm):
    class Meta:
        model = custom_user
        fields = ['username', 'lastname', 'firstname', 'email', 'password']

class todoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields['add_item','confirm','created_at']
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)