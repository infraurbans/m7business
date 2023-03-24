from django.shortcuts import render
from django.views.generic.list import ListView

from m7.contracts.models import Contract

class MyContracts(ListView):
    model = Contract
    paginate_by = 100
    template_name="dashboard/contracts/my_contracts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

my_contracts = MyContracts.as_view()