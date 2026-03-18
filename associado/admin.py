from django.contrib import admin
from .models import Associado

@admin.register(Associado)
class AssociadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'matricula', 'status', 'data_cadastro')
    search_fields = ('nome', 'email', 'matricula')
    list_filter = ('status', 'data_cadastro')

# Register your models here.
