from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def registrationform(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "Sorry the username is taken, try another one")
            return redirect("registrationform")


        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            
        )

        user.set_password(password)
        user.save()
        messages.info(request, "account created successfully")
        return redirect('registrationform')






    return render(request, "registration/registrationform.html")


@login_required(login_url='loginPage')
def homepage(request):
    return render(request, 'index.html')


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        

        if  not User.objects.filter(username = username).exists():
            messages.error(request, "Invalid Username")
            return redirect('loginPage')
        

        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "invalid password")
            return redirect("loginPage")
        else:
            login(request, user)
            return redirect("homepage")




    return render(request, 'registration/loginPage.html')


def logoutPage(request):
    logout(request)
    return redirect('loginPage')

    
