from django.shortcuts import render
from django.views.generic.list import ListView

from m7.dividends.models import Dividend
from m7.contracts.models import Contract
from django.contrib.auth.mixins import LoginRequiredMixin


class MyDividends(LoginRequiredMixin, ListView):
    model = Dividend
    paginate_by = 100
    template_name = "dashboard/dividends/my_dividends.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        request = self.request
        q_contract = request.GET.get("q_contract", None)
        if q_contract:
            context["contract"] = Contract.objects.filter(
                pk=q_contract, user=self.request.user
            ).first() or None 
            
        return context
    
    def get_queryset(self):
        request = self.request
        q_contract = request.GET.get("q_contract", None)
        queryset = super(MyDividends, self).get_queryset()
        queryset = queryset.filter(contract__user=self.request.user)

        if q_contract:
            queryset = queryset.filter(contract=q_contract)

        return queryset


my_dividends = MyDividends.as_view()
