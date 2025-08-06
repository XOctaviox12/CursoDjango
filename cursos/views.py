from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from .models import Curso

def cursos(request):
    """Vista para listar todos los cursos"""
    try:
        cursos = Curso.objects.all().order_by('-fecha_creacion')
        return render(request, "cursos/cursos.html", {'cursos': cursos})
    except Exception as e:
        # Log the error (implementar logging adecuado en producción)
        return render(request, "error.html", {
            'error': "Ocurrió un error al recuperar los cursos",
            'detalle': str(e)
        })

def editar_curso(request, id):
    """Vista para editar un curso existente"""
    curso = get_object_or_404(Curso, id=id)
    
    if request.method == 'POST':
        try:
            # Actualización de campos básicos
            curso.nombre = request.POST.get('nombre', curso.nombre)
            curso.descripcion = request.POST.get('descripcion', curso.descripcion)
            
            # Campos numéricos con validación
            curso.duracion = int(request.POST.get('duracion', curso.duracion))
            curso.precio = float(request.POST.get('precio', curso.precio))
            
            # Nivel con validación de opciones
            nivel = request.POST.get('nivel', curso.nivel)
            if nivel in dict(Curso.NIVELES).keys():
                curso.nivel = nivel
            
            # Manejo de imagen (opcional)
            if 'imagen' in request.FILES:
                curso.imagen = request.FILES['imagen']
            
            # Disponibilidad como booleano
            curso.disponible = request.POST.get('disponible') == 'on'
            
            curso.save()
            return redirect('cursos')
            
        except (ValueError, TypeError) as e:
            return render(request, 'cursos/editarCurso.html', {
                'curso': curso,
                'error': f"Error en los datos numéricos: {str(e)}"
            })
        except Exception as e:
            return render(request, 'cursos/editarCurso.html', {
                'curso': curso,
                'error': f"Ocurrió un error al actualizar: {str(e)}"
            })
    
    return render(request, 'cursos/editarCurso.html', {'curso': curso})

def crear_curso(request):
    """Vista para crear un nuevo curso"""
    if request.method == 'POST':
        try:
            # Validación de campos requeridos
            required_fields = ['nombre', 'descripcion', 'duracion', 'precio', 'nivel']
            for field in required_fields:
                if not request.POST.get(field):
                    raise ValidationError(f"El campo {field} es requerido")
            
            # Validación del nivel
            nivel = request.POST['nivel']
            if nivel not in dict(Curso.NIVELES).keys():
                raise ValidationError("Nivel inválido seleccionado")
            
            # Creación del curso con el modelo simplificado
            curso = Curso(
                nombre=request.POST['nombre'],
                descripcion=request.POST['descripcion'],
                duracion=int(request.POST['duracion']),
                nivel=nivel,
                precio=float(request.POST['precio']),
                disponible=request.POST.get('disponible') == 'on',
                imagen=request.FILES.get('imagen')
            )
            
            curso.save()
            return redirect('cursos')
            
        except ValidationError as e:
            return render(request, 'cursos/crearCurso.html', {
                'error': str(e),
                'form_data': request.POST
            })
        except (ValueError, TypeError) as e:
            return render(request, 'cursos/crearCurso.html', {
                'error': f"Error en los datos numéricos: {str(e)}",
                'form_data': request.POST
            })
        except Exception as e:
            return render(request, 'cursos/crearCurso.html', {
                'error': f"Error al crear el curso: {str(e)}",
                'form_data': request.POST
            })
    
    return render(request, 'cursos/crearCurso.html')

def eliminar_curso(request, id):
    """Vista para eliminar un curso"""
    curso = get_object_or_404(Curso, id=id)
    
    if request.method == 'POST':
        try:
            curso.delete()
            return redirect('cursos')
        except Exception as e:
            return render(request, 'cursos/confirmarEliminacion.html', {
                'object': curso,
                'error': f"Error al eliminar el curso: {str(e)}"
            })
    
    return render(request, 'cursos/confirmarEliminacion.html', {'object': curso})