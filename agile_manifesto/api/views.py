from django.shortcuts import render
from rest_framework import viewsets
from .models import Value, Principle
from .serializers import ValueSerializer, PrincipleSerializer

from django.urls import reverse


class ValueView(viewsets.ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


class PrincipleView(viewsets.ModelViewSet):
    queryset = Principle.objects.all()
    serializer_class = PrincipleSerializer
