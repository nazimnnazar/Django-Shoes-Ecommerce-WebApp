from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import auth
from . forms import SignUpForm


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,("You are Successfully! Log In!!!!!"))
            return redirect('/')
        else:
            messages.success(request,("The User name or password incorrect!!!"))
            return redirect('login')
    else:
        return render(request,'core/login.html')

def logout(request):
    auth.logout(request)
    messages.success(request,("You are successfully LogOut!!!"))
    return redirect('/')

def register(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth.login(request,user)
            messages.success(request,("You are successfully Register!!!"))
            return redirect('/')
    else:
        messages.success(request,("Oops!!! Please enter Courect form"))
        form =SignUpForm()
    context={
        'form':form
        }
    return render(request,'core/register.html',context)