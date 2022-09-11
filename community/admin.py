from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import Board, Comment, Liked

# Register your models here.
admin.site.register(Board)
admin.site.register(Comment)
admin.site.register(Liked)