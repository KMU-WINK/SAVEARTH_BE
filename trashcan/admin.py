from django.contrib import admin
from .models import Trashcan

class TrashcanAdmin(admin.ModelAdmin):
    model = Trashcan
    list_display = ['id', 'user_id__id']

    

# admin.site.register(Trashcan)