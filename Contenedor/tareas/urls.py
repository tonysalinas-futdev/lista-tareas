from django.urls import path
from .views import ver_tareas, crear_tarea, ver_detalles, actualizar_tarea, eliminar_tarea

urlpatterns = [
    path("tareas_todas/", ver_tareas, name="Tareas"),
    path("crear_tarea/", crear_tarea, name="Crear"),
    path("detalles_tarea/<int:tarea_id>", ver_detalles ,name="detalles"),
    path("actualizar_la_tarea/<int:tarea_id>", actualizar_tarea, name="actualizar" ),
    path("eliminar_tarea/<int:tarea_id>", eliminar_tarea ,name="eliminar"),

]