from django.contrib import admin
from core.models import Evento

# Register your models here.
class EvendoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'id', 'descricao', 'data_evento', 'data_criacao')
    list_filter = ('usuario', 'data_evento',)




admin.site.register(Evento, EvendoAdmin)