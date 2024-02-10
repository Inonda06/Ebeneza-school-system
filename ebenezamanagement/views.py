from django.shortcuts import render,redirect
from django.contrib import  messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def Landingpage(request):
    return render(request,'home.html')
    
def admindashboard(request):
    return render(request,'admindashboard.html')

def Loginpage(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('ebenezamanagement:admin')

        else:
            messages.error(request,'username or Password is Incorrect')
    context={}
    return render(request,'Login.html',context)