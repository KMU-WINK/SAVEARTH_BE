from django.contrib import admin
from .models import Trash

class TrashAdmin(admin.ModelAdmin):
    model = Trash
    list_display = ['id']