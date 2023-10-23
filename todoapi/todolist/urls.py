from django.urls import path
from .views import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import  View

app_name = 'todolist'
class LibroAPI(View):
    def post(self, request, *args, **kwargs):
        # Obtén los datos JSON de la solicitud POST
        datos = json.loads(request.body)

        # Aquí puedes manejar los datos, por ejemplo, guardarlos en la base de datos

        # Devuelve una respuesta JSON indicando que el libro ha sido creado
        return JsonResponse({"mensaje": "Libro creado exitosamente!"})


urlpatterns = [
    # Otras rutas de tu aplicación...
    path('api/libros/', csrf_exempt(LibroAPI.as_view()), name='libro-api'),
    path('v1/post', Post_APIView.as_view()),
    path('v1/post/<int:pk>/', Post_APIView_Detail.as_view()),
]
