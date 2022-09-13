from rest_framework import serializers
from .models import Matches

class MatchesSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Matches # tell django which model to use
        fields = ('id', 'name', 'intelligence', 'strength', 'speed','durability','power','combat',)
