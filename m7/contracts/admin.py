from django.contrib import admin
from m7.contracts.models import Contract
from m7.dividends.models import Dividend
# Register your models here.


class DividendInline(admin.TabularInline):
    model = Dividend
    extra = 1

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('user', 'contribution', 'duration', 'payment_day', 'percent', 'start_at',)
    inlines = (DividendInline, )
