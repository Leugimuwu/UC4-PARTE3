from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', views.saludo, name = "saludo"),
    path('integrantes/', views.integrantes, name = "integrantes"),
]