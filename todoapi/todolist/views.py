from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

# Vista para la página de inicio

def index(request):
    items = Item.objects.all()  # Obtén todos los items de la base de datos
    return render(request, 'index.html', {'items': items})

# Vista para crear un nuevo item
def crear_item(request):
    # Aquí puedes manejar la lógica para crear un nuevo item
    return HttpResponse("Página para crear un nuevo item")

# Vista para ver detalles de un item por su ID
def ver_item(request, item_id):
    item = Item.objects.get(pk=item_id)  # Obtén el item por su ID desde la base de datos
    return render(request, 'ver_item.html', {'item': item})

# Vista para editar un item por su ID
def editar_item(request, item_id):
    # Aquí puedes manejar la lógica para editar un item existente
    return HttpResponse(f"Página para editar el item con ID {item_id}")

# Vista para eliminar un item por su ID
def eliminar_item(request, item_id):
    # Aquí puedes manejar la lógica para eliminar un item existente
    return HttpResponse(f"Página para eliminar el item con ID {item_id}")
