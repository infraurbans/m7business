from django.contrib import admin
from m7.contracts.models import Contract
# Register your models here.


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    pass
