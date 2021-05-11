from django.shortcuts import render
from rest_framework import viewsets

from api.models import Fix
from api.serializers import FixSerializer


class FixViewSet(viewsets.ModelViewSet):
    queryset = Fix.objects.all()
    serializer_class = FixSerializer
