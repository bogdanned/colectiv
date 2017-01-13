from django.contrib import admin
from .models import *
# Register your models here.

class RouteAdmin(admin.ModelAdmin):
    list_display = ['id','origin', 'destiny']

admin.site.register(Route, RouteAdmin)
