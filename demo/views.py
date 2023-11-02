from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def landing (request):
    return render(request,'landing.html')
def aboutus (request):
    return render(request,'aboutus.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,'Invalid')
            return redirect('index')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Used')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not the same')
            return redirect('login')
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def firRegistration (request):
    return render(request,'index.html')

def showupdate (request):
    return render(request,'landing.html')

def addinfo (request):
    return render(request,'landing.html')

def emergencyContact (request):
    return render(request,'landing.html')

def crimeRecord (request):
    return render(request,'landing.html')


def  index (request):
    return render(request,'index.html')
