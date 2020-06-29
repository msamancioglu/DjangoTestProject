from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal
from .serializers import AnimalSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


def showanimal(request):
    return  HttpResponse('animals here')


class AnimalListAPIView(generics.ListCreateAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


