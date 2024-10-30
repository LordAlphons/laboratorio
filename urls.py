from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('insertar/', views.insertar_lab, name='insertar-lab'),
 path('editar/<int:pk>/', views.editar_lab, name='editar-lab'),
 path('editar/actualizar/<int:id>/', views.actualizar_laboratorio, name='actualizar-laboratorio'),
 path('eliminar/<int:pk>/', views.eliminar_lab, name='eliminar-lab'),
]