from django.contrib import admin

from . import models

# Register your models here.

from m7.core.models import Contract, Dividend


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass


@admin.register(Dividend)
class DividendAdmin(admin.ModelAdmin):
    pass
