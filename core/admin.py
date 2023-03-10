from django.contrib import admin

from . import models

# Register your models here.

from models import Contratos

from models import Dividendos


@admin.register(Contratos)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'Aporte', 'Prazo', 'Pagamento_dia')


@admin.register(Dividendos)
class DividendoAdmin(admin.ModelAdmin):
    list_display = ('Contrato', 'Valor', 'Data', 'Comprovante', 'Ordem')