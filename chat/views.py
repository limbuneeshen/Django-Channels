from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def chat(request):
    return render(request,'chat.html',{})

def Login(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
      if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         if username and password:
            user = authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect("index")
    return render(request,'login.html',{})

def signup(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
       if request.method == 'POST':
           username = request.POST['username']
           password = request.POST['password']
           email = request.POST['email'] 
           user = User.objects.create(username=username,email=email,password=password)
           if user:
              return redirect("login")
    return render(request,'signup.html',{})