from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nivel', 'costo', 'fecha_creacion')
    list_filter = ('nivel',)
    search_fields = ('nombre',)
    date_hierarchy = 'fecha_creacion'
    ordering = ['fecha_creacion']
    readonly_fields = ('fecha_creacion',)
