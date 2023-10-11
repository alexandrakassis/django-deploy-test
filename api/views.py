from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import CycleSerializer
from .models import Cycle
# Create your views here. THis is where we right our endpoints
# view a list of all the cycles that ran

# an api view that letsus view a list of all cycles run.
# a view already set up to return all the cycle objects and converts it 
# into a format that can be read
class CycleView(generics.CreateAPIView):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
    
