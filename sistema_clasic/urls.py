"""
URL configuration for sistema_clasic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.tablesjoin, name='inicio'),
    path('crear_pais', views.crear_pais, name='crear_pais'),
    path('crear_estado', views.crear_estado, name='crear_estado'),
    path('cargar_estado', views.cargar_estado, name='cargar_estado'),
    path('editar_estado', views.editar_estado, name='editar_estado'),
]
