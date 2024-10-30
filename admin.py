from django.contrib import admin
from .models import DirectorGeneral, Laboratorio, Producto

class LaboratorioAdmin(admin.ModelAdmin):
 list_display = ('id', 'nombre')
 search_fields = ('id', 'nombre')
 ordering = ('nombre',)

class DirectorGeneralAdmin(admin.ModelAdmin):
 list_display = ('id', 'nombre', 'laboratorio')
 search_fields = ('id', 'nombre', 'laboratorio')
 ordering = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
 list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
 search_fields = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
 ordering = ('nombre',)
 list_filter = ('nombre', 'laboratorio')

admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(Producto, ProductoAdmin)