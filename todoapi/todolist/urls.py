from django.urls import path
from . import views
from django.urls import reverse

app_name = 'todolist'
# Define un espacio de nombres para evitar conflictos de nombres de URL en diferentes aplicaciones

urlpatterns = [
    # Vista para la página de inicio
    path('', views.index, name='index'),

    # Vista para crear un nuevo item
    path('crear/', views.crear_item, name='crear_item'),

    # Vista para ver detalles de un item por su ID
    path('item/<int:item_id>/', views.ver_item, name='ver_item'),

    # Vista para editar un item por su ID
    path('item/<int:item_id>/editar/', views.editar_item, name='editar_item'),

    # Vista para eliminar un item por su ID
    path('item/<int:item_id>/eliminar/', views.eliminar_item, name='eliminar_item'),


]
