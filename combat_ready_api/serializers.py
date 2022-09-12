from rest_framework import serializers
from .models import Contact

class CombatantSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Combatant # tell django which model to use
        fields = ('id', 'name', 'intelligence', 'strength', 'speed','durability','power','combat',)
