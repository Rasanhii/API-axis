from rest_framework import serializers
from lista.models import Produtos

class ListaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produtos
        fields = [ 'id', 'nome', 'quantidade', 'preco', 'descricao' ]
