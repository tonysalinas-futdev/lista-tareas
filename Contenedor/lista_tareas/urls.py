
from django.contrib import admin
from django.urls import path, include
from tareas.views  import home
from login.views import signin, loguear,cerrar_sesion


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("Sign-In", signin, name="autenticarse"),
    path("login", loguear, name="loguearse"),
    path("cerrar_sesion", cerrar_sesion, name="logout"),

    
    
    path("tareas/", include("tareas.urls")),
]
