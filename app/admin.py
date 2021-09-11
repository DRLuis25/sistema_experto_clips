from django.contrib import admin
from .models import Sintoma
#Register your models here

class SintomaAdmin(admin.ModelAdmin):
    search_fields = ['descripcion']
    list_per_page = 10

admin.site.register(Sintoma, SintomaAdmin)