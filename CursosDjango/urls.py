"""
URL configuration for CursosDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from contenido import views
from cursos import views as views_cursos
from django.conf import settings

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', views.principal, name="principal"),
    path('contacto/', views.contacto, name="contacto"),
    # path('cursos/', views.cursos, name="cursos"),
    path('cursos/', views_cursos.cursos, name="cursos"),
    path('crearCursos/', views_cursos.crear_curso, name="agregar_curso"),
    path('EditarCurso/<int:id>/', views_cursos.editar_curso, name='Editar'),
    path('eliminarComentario/<int:id>/', views_cursos.eliminar_curso,name='Eliminar'),
]
if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)