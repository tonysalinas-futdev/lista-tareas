from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import TareaForm
from .models import Tarea

def home(request):
    return render (request, "home.html")


def ver_tareas(request):
    tareas=Tarea.objects.all().order_by("-fecha_creacion")
    return render (request, "listado-tareas.html", {
        "tareas": tareas
    })


def crear_tarea(request):
    if request.method=="POST":
        form=TareaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Ha creado la tarea satisfactoriamente")
            return redirect("Tareas")
        else:
            messages.error(request, "El formulario tiene errores")
    else:
        form=TareaForm()
    return render(request, "crear_tarea.html", { "form":form
    })

def ver_detalles(request, tarea_id):
    tarea=get_object_or_404(Tarea,id=tarea_id)
    return render(request, "detalles.html", {"tarea":tarea})

def actualizar_tarea(request, tarea_id):
    tarea=get_object_or_404(Tarea, id=tarea_id)
    form=TareaForm(request.POST or None, instance=tarea)
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("Tareas")
    return render(request, "actualizar.html",{"form":form})