from django.contrib import admin
from django.utils.html import format_html
from .models import *

class PlantasAdmin(admin.ModelAdmin):
    list_display = ("nombre","image")

# Register your models here.

admin.site.register(Plantas,PlantasAdmin)
admin.site.register(Jardines)
admin.site.register(Cultivos)
admin.site.register(Contactos)
admin.site.register(Reproduccion)
