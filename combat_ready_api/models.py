from django.db import models

# Create your models here.
class Matches(models.Model):
    matchName = models.CharField(max_length=40, default = '')

    nameP1 = models.CharField(max_length=40, default = '')
    realNameP1 = models.CharField(max_length=60, default = '')
    speciesP1 = models.CharField(max_length=60, default = '')
    intelligenceP1 = models.IntegerField(default = 0)
    strengthP1 = models.IntegerField(default = 0)
    speedP1 = models.IntegerField(default = 0)
    durabilityP1 = models.IntegerField(default = 0)
    powerP1 = models.IntegerField(default = 0)
    imageP1 = models.TextField(default = '')

    nameP2 = models.CharField(max_length=40, default = '')
    realNameP2 = models.CharField(max_length=60, default = '')
    speciesP2 = models.CharField(max_length=60, default = '')
    intelligenceP2 = models.IntegerField(default = 0)
    strengthP2 = models.IntegerField(default = 0)
    speedP2 = models.IntegerField(default = 0)
    durabilityP2 = models.IntegerField(default = 0)
    powerP2 = models.IntegerField(default = 0)
    imageP2 = models.TextField(default = '')

class Stage(models.Model):
    nameOfStage = models.CharField(max_length=500, default='0000000')

    

