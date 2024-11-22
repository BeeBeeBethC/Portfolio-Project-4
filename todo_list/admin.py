from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import person

# Register your models here.


@admin.register(person)
class ToDoAdmin(SummernoteModelAdmin):

    list_display = ('username', 'firstname', 'lastname', 'email', 'is_staff')
    search_fields = ['username', 'email', 'is_staff']
    # list_filter = ('status',)
    summernote_fields = ('content',)