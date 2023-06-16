from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import *
from django.contrib import messages
from .forms import *
from django.urls import reverse
from .models import *

username = ''
def authenticate(request, model, username=None, password=None):
    try:
        user = model.objects.get(username=username)
        if user.password == password:
            return user
    except model.DoesNotExist:
        pass
    return None
    
def register(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        }
    return render(request, 'register.html', context)

def ngo_register(request):
    form = NGO_RegForm(request.POST)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
        }
    return render(request, 'NGOregister.html', context)

def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request=request, model = Volunteer, username=username, password=password)

        if user:
            return HttpResponseRedirect('http://127.0.0.1:8000/appone/volunteer')
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'login.html', {})

def ngo_login_view(request):
    global username
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, model = NGO, username=username, password=password)

        if user:
            r = open('x.txt','w')
            r.write(username)
            r.close()
            return render(request,'NGOportal.html',context={'ngo':NGO.objects.get(username=username)})
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'NGOlogin.html', {})
    
def ngoportal(request):
    return render(request,'NGOportal.html')

def volunteer(request):
    return render(request,'VolunteerRedirect.html')

def ngosearch(request):
    return render(request,'ngosearch.html')

def blogview(request):
    return render(request,'blogpage.html')

def dropdown_view(request):
    return render(request,'dropdown.html')

def ngoportal(request):
    r = open('x.txt','r')
    username = r.read()
    r.close()
    if request.method == "POST":
        user = NGO.objects.get(username = username)
    return render(request,'NGOportal.html',context={'ngo':user})


def newblog(request):
    return render(request,'newblog.html')
