from django.contrib import admin

from .models import Farmacia
from .models import Turno


class FarmaciaAdmin(admin.ModelAdmin):
	list_display = ('nombre','direccion','telefono')
	#list_filter = ('editor', 'estado')
	#ordering = ('fecha_publicacion',)
	#search_fields = ('autor','editor',)

class TurnoAdmin(admin.ModelAdmin):
	list_display = ('fecha','farmacia','tipo')
	list_filter = ('fecha','farmacia','tipo')
	ordering = ('fecha',)
	search_fields = ['fecha','farmacia__nombre']


admin.site.register(Farmacia, FarmaciaAdmin)
admin.site.register(Turno, TurnoAdmin)
