from dataclasses import fields
from rest_framework import serializers
from .models import Matches
from .models import Stage

class MatchesSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Matches # tell django which model to use
        fields = ('id', 'matchName', 'nameP1', 'realNameP1', 'speciesP1', 'intelligenceP1', 'strengthP1', 'speedP1','durabilityP1','powerP1','imageP1', 'nameP2', 'realNameP2', 'speciesP2', 'intelligenceP2', 'strengthP2', 'speedP2','durabilityP2','powerP2','imageP2',)
class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ('id', 'nameOfStage',)

