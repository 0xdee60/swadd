from django.contrib import admin
from .models import Prueba
# Register your models here.

class PruebaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre_completo',)}
    list_display = ('nombre_completo','slug')


admin.site.register(Prueba, PruebaAdmin)

