from django.contrib import admin
from .models import Curso, Actividad
from django.utils.html import format_html
from django.contrib.admin import AdminSite

class GladeliAdminSite(AdminSite):
    site_header = 'Administración Gladeli'
    site_title = 'Gladeli - Sistema de Cursos'
    index_title = 'Panel de Control'
    site_url = '/'  # Enlaza al sitio principal
    
    def each_context(self, request):
        context = super().each_context(request)
        context['site_header'] = self.site_header
        context['site_title'] = self.site_title
        context['index_title'] = self.index_title
        return context

gladeli_admin = GladeliAdminSite(name='gladeliadmin')

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_nivel_display', 'precio', 'precio_formateado', 'duracion', 'disponible_badge')  # Añadí 'precio'
    list_filter = ('nivel', 'disponible', 'fecha_creacion')
    search_fields = ('nombre', 'descripcion')
    list_editable = ('duracion', 'precio')  # 'precio' ahora está en list_display
    readonly_fields = ('fecha_creacion', 'precio_formateado', 'disponible_badge')
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'nivel')
        }),
        ('Detalles del Curso', {
            'fields': ('precio', 'duracion', 'imagen')
        }),
        ('Disponibilidad', {
            'fields': ('disponible', 'fecha_creacion')
        }),
    )
    
    def precio_formateado(self, obj):
        return f"${obj.precio:,.2f}"
    precio_formateado.short_description = 'Precio Formateado'  # Cambié el nombre para diferenciar
    
    def disponible_badge(self, obj):
        color = 'success' if obj.disponible else 'secondary'
        texto = 'Disponible' if obj.disponible else 'No disponible'
        return format_html(
            '<span class="badge badge-{}">{}</span>',
            color, texto
        )
    disponible_badge.short_description = 'Estado'

admin.site.register(Curso, CursoAdmin)


from django.contrib import admin
from .models import Actividad

class ActividadAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_curso', 'descripcion', 'created')  # muestra también la fecha en la tabla
    search_fields = ('id',)  # 'created' no es buena para búsqueda de texto
    # date_hierarchy = 'created'  # correcto: este campo sí existe
    readonly_fields = ('created', 'id')  # evita modificar esos campos

admin.site.register(Actividad, ActividadAdmin)

