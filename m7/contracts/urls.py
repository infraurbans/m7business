from django.urls import path

from m7.contracts.views import my_contracts

app_name = "contracts"

urlpatterns = [
    path('meus-contratos', my_contracts, name="my_contracts"),
]
