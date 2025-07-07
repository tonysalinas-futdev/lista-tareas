from django.urls import path
from .views import ver_tareas

urlpatterns = [
    path("tareas_todas/", ver_tareas, name="Tareas")
]