from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import CombatantSerializer
from .models import Combatant

class CombatantList(generics.ListCreateAPIView):
    queryset = Combatant.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = CombatantSerializer # tell django what serializer to use

class CombatantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Combatant.objects.all().order_by('id')
    serializer_class = CombatantSerializer
