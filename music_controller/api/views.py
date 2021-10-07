from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import generic
from .models import Room
from .serializers import RoomSerializer

# Create your views here.
# def main(request):
#     return HttpResponse("<h1>Hello")
class RoomView(generic.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
