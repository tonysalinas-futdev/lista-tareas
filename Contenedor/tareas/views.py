from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from .forms import TareaForm
from .models import Tarea
from django import http

#Vista para pantalla de incio
def home(request):
    return render (request, "home.html")

#Vista para ver todas las tareas
@login_required
def ver_tareas(request):
    tareas=Tarea.objects.filter(usuario=request.user).order_by("-fecha_creacion")
    return render (request, "listado-tareas.html", {
        "tareas": tareas
    })

#Vista para crear tarea
@login_required

def crear_tarea(request):
    if request.method=="POST":
        form=TareaForm(request.POST)
        if form.is_valid():
            tarea=form.save(commit=False)
            tarea.usuario=request.user
            tarea.save()
            messages.success(request,"Ha creado la tarea satisfactoriamente")
            return redirect("Tareas")
        else:
            messages.error(request, "El formulario tiene errores")
    else:
        form=TareaForm()
    return render(request, "crear_tarea.html", { "form":form
    })

#Vista para ver los detaelles de la tarea
@login_required

def ver_detalles(request, tarea_id):
    tarea=get_object_or_404(Tarea,id=tarea_id, usuario=request.user)
    return render(request, "detalles.html", {"tarea":tarea})


#Vista para actualizar la tarea
@login_required

def actualizar_tarea(request, tarea_id):
    tarea=get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
    
    if request.method == 'POST':
        form = TareaForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save()
            return redirect("Tareas")
    else:
        form=TareaForm(instance=tarea)
    return render(request, "actualizar.html",{"form":form})

#Vista para eliminar la tarea
@login_required

def eliminar_tarea(request, tarea_id):
    tarea=get_object_or_404(Tarea,id=tarea_id, usuario=request.user)
    tarea.delete()
    messages.success(request, "La Tarea ha sido eliminada con éxito ")
    return redirect("Tareas")
    

@login_required
def completar_tarea(request, tarea_id):
    tarea=get_object_or_404(Tarea, id=tarea_id, usuario=request.user)
    tarea.completada=True
    tarea.save()
    return redirect("Tareas")