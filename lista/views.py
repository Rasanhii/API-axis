from rest_framework import viewsets
from lista.models import Produtos
from lista.serializer import ListaSerializer

class ListaViewSet(viewsets.ModelViewSet):
    """Endpoint para exibir dados da lista"""
    queryset = Produtos.objects.all()
    serializer_class = ListaSerializer


