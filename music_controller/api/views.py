from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room


class RoomView(generics.ListAPIView):     # this will return to us all the room views
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


