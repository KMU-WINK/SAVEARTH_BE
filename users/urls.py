from django.urls import path
from . import views

urlpatterns =[
    path('signup/', views.UserCreate.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('getuser/', views.UserView.as_view()),
 ]