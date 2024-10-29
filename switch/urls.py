from django.urls import path
from .views import CadastroSw, ListaSw, EditaSw


urlpatterns = [
    path('cadastro-switch/', CadastroSw.as_view(), name='cadastro_sw'),
    path('lista-switch/', ListaSw.as_view(), name='lista_sw'),
    path('edita_switch/<int:pk>', EditaSw.as_view(), name='edita_sw'),
]