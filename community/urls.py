from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('write', views.write),
    path('insert', views.insert),
    path('detail', views.detail),
    path('update', views.update),
    path('delete', views.delete),
    path('reply_insert', views.reply_insert),
]