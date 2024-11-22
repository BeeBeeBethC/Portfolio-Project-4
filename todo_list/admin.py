from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ToDo

# Register your models here.


@admin.register(ToDo)
class ToDoAdmin(SummernoteModelAdmin):

    list_display = ('add_item', 'confirm', 'created_at')
    search_fields = ['created_at']
    # list_filter = ('status',)
    summernote_fields = ('content',)