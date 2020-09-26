from django.urls import path
from persona import views

urlpatterns = [
    path('caminantes/', views.lista_caminantes),
]
