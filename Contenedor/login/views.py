from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages


def signin(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            messages.success(request,"Usted se ha autenticado satisfactoriamente")
            return redirect("home")
    else:
        form=SignUpForm()

    return render(request,"signup.html",{"form":form})


def loguear(request):
    if request.user.is_authenticated:
        messages.warning(request,"Usted ya esta autenticado")
        return redirect("Tareas")
    if request.method=="POST":
        form=LoginForm(request.POST, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect ("home")
    else:
        form=LoginForm()
    return render(request,"loguearse.html",{"form":form})
        

def cerrar_sesion(request):
    logout(request)
    return redirect("home")