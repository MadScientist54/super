from django.urls import path
from .views import CadastroPC, ListaPC, EditaPC

urlpatterns = [
    path('cadastro-pc/', CadastroPC.as_view(), name='cadastro_pc'),
    path('lista-pc/', ListaPC.as_view(), name='lista_pc'),
    path('edita-pc/<int:pk>', EditaPC.as_view(), name='edita_pc'),
]
