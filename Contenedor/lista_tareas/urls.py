
from django.contrib import admin
from django.urls import path, include
from tareas.views  import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("tareas/", include("tareas.urls"))
]
