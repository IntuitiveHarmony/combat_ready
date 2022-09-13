from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import MatchesSerializer
from .models import Matches

class MatchesList(generics.ListCreateAPIView):
    queryset = Matches.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = MatchesSerializer # tell django what serializer to use

class MatchesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Matches.objects.all().order_by('id')
    serializer_class = MatchesSerializer
