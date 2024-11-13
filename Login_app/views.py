from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

def sign_up(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,password=password)
        if user is not None:
            return redirect('login_page')
    return render(request,'sign_up.html')   

def login_page(request):
    error_message=None
    if request.POST:
        username=request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('view')
        else:
            error_message="Invalid Credentials"

    return render(request,'login.html',{'error_message':error_message})

def logout_page(request):
    logout(request)
    return redirect('index')


