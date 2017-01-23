from django.contrib import admin
from .models import *
# Register your models here.

class RouteAdmin(admin.ModelAdmin):
    list_display = ['user','id', 'origin', 'destiny', 'duration', 'distance', 'created']

admin.site.register(Route, RouteAdmin)
admin.site.register(Email)
