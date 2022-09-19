from django.contrib import admin

# Register your models here.
from .models import Matches, Stage
admin.site.register(Matches)
admin.site.register(Stage)
