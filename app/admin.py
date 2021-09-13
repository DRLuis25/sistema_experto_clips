from django.contrib import admin
from .models import Sintoma,Diagnostico,DiagnosticoUsuario
#Register your models here

class SintomaAdmin(admin.ModelAdmin):
    search_fields = ['descripcion']
    list_per_page = 10

class DiagnosticoAdmin(admin.ModelAdmin):
    search_fields = ['resultado']
    list_per_page = 10

class DiagnosticoUsuarioAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_per_page = 10
    list_display = ('name','diagnostic')

admin.site.register(Sintoma, SintomaAdmin)
admin.site.register(Diagnostico, DiagnosticoAdmin)
admin.site.register(DiagnosticoUsuario, DiagnosticoUsuarioAdmin)