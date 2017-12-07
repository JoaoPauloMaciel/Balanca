from django.contrib.auth.models import User, Group
from balanca.models import Pesagem, Mensagem
from rest_framework import serializers

class PesosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pesagem
        fields = ('url','peso','data','usuario')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    pesos = PesosSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email','password', 'groups','pesos')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class MensagemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mensagem
        fields = ('url','conteudo')

