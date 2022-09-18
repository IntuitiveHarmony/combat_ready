from django.db import models

# Create your models here.
class Matches(models.Model):
    matchName = models.CharField(max_length=40, default = '')

    nameP1 = models.CharField(max_length=40, default = '')
    realNameP1 = models.CharField(max_length=60, default = '')
    speciesP1 = models.CharField(max_length=60, default = '')
    intelligenceP1 = models.CharField(max_length=5, default = '')
    strengthP1 = models.CharField(max_length=5, default = '')
    speedP1 = models.CharField(max_length=5, default = '')
    durabilityP1 = models.CharField(max_length=5, default = '')
    powerP1 = models.CharField(max_length=5, default = '')
    imageP1 = models.TextField(max_length=5, default = '')

    nameP2 = models.CharField(max_length=40, default = '')
    realNameP2 = models.CharField(max_length=60, default = '')
    speciesP2 = models.CharField(max_length=60, default = '')
    intelligenceP2 = models.CharField(max_length=5, default = '')
    strengthP2 = models.CharField(max_length=5, default = '')
    speedP2 = models.CharField(max_length=5, default = '')
    durabilityP2 = models.CharField(max_length=5, default = '')
    powerP2 = models.CharField(max_length=5, default = '')
    imageP2 = models.TextField(default = '')

class Stage(models.Model):
    nameOfStage = models.CharField(max_length=100, default='0000000')
