from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from django.conf.urls import url, include
from rest_framework import routers, serializers, viewsets


class Pesagem(models.Model):
    peso = models.IntegerField(null=True)
    data = models.DateTimeField('date da pesagem', default=timezone.now)
    usuario = models.ForeignKey(User ,null=True)


class Mensagem(models.Model):
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)
    conteudo = models.CharField(max_length=400)
    #votes = models.IntegerField(default=0)
