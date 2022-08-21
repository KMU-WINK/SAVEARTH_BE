from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print('인증')
            login(request, user)
        else:
            print('노노')
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("user:login")

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        nickname = request.POST["nickname"]
        birth_year = request.POST["birth_year"]
        birth_month = request.POST["birth_month"]
        birth_day = request.POST["birth_day"]
        gender = request.POST["gender"]

        user = User.objects.create_user(username, '', password)     
        user.nickname = nickname
        user.birth_year = birth_year
        user.birth_month = birth_month
        user.birth_day = birth_day  
        user.gender = gender
        user.save()
        return redirect("user:login")
        
    return render(request, "users/signup.html")