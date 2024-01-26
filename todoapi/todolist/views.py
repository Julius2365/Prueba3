from django.shortcuts import render,redirect
from django.http import HttpResponse , Http404
from .models import Item
from .forms import ItemForm



# Vista para la página de inicio

def index(request):
    items = Item.objects.all()  # Obtén todos los items de la base de datos
    return render(request, 'index.html', {'items': items})

# Vista para crear un nuevo item
def crear_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario aquí
            form.save()  # Esto guarda el objeto Producto en la base de datos
            return redirect('index')

    else:
        form = ItemForm()

    return render(request, 'crear_item.html',{'form':form})

# Vista para ver detalles de un item por su ID
def ver_item(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
    except Item.DoesNotExist:
        raise Http404("El libro no esta registrado")  # Puedes personalizar este mensaje según tus necesidades
    return render(request, 'ver_item.html', {'item': item})
# Vista para editar un item por su ID
def editar_item(request,item_id):
    if item_id:
        # Edición de un producto existente
        item = Item.objects.get(pk=item_id)
        if request.method == 'POST':
            form = ItemForm(request.POST, instance=item)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = ItemForm(instance=item)
    else:
        # Creación de un nuevo producto
        if request.method == 'POST':
            form = ItemForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
        else:
            form = ItemForm()

    return render(request, 'editar_item.html',{'form':form})

# Vista para eliminar un item por su ID
def eliminar_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    return redirect('index')