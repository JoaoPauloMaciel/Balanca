from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from balanca.serializers import UserSerializer, GroupSerializer, PesosSerializer, MensagemSerializer

from balanca.models import Pesagem, Mensagem


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PesosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Pesagem.objects.all()
    serializer_class = PesosSerializer

class MensagemViewSet(viewsets.ModelViewSet):

    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer


def index(request):
    return HttpResponse("Hello, world. Essa é a view da balança!")

