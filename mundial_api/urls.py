from django.urls import path

from mundial_api import views


urlpatterns = [
    path('equipo1/', views.listaEquipo),
    path('equipo/', views.listaEquipo2),
    path('equipo/<int:id>', views.mostrarEquipo),
    path('equipo1/<int:id>', views.mostrarEquipo2),
    path('jugador/editar/<int:id>', views.gestionarJugador),
]