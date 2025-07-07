from django.shortcuts import render
from .models import Tarea

def home(request):
    return render (request, "home.html")


def ver_tareas(request):
    tareas=Tarea.objects.all().order_by("-fecha_creacion")
    return render (request, "listado-tareas.html", {
        "tareas": tareas
    })


