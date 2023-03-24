from django.contrib import admin
from m7.dividends.models import Dividend

@admin.register(Dividend)
class DividendAdmin(admin.ModelAdmin):
    pass
