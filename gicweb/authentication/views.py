from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]  # or request.POST["last_name"] if form uses that
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email Taken')
            return redirect('register')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=firstname,
                last_name=lastname  # must be passed
            )
            user.save()
            messages.success(request, "Registration successful!")
            return redirect('login')
    messages.error(request,"Registration Faild")
    return render(request, 'register.html')

def login_auth(request):
    if request.method=="POST":
        data=request.POST
        username=data["username"]
        password=data["password"]
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request,'register.html')

@login_required(login_url='login')
def logout_auth(request):
    logout(request)
    return redirect('login')
