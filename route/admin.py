from django.contrib import admin
from .models import Route

class RouteAdmin(admin.ModelAdmin):
    model = Route
    list_display = ['id']
