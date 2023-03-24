from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.db.models import Sum
from m7.contracts.models import Contract
from m7.dividends.models import Dividend

class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['my_contracts'] = user.contract_set.all()[:5]
        context['total_contracts'] = user.get_total_count_contracts()
        context['total_contribution'] = user.get_total_contributions()
        context['total_contributions_activies_contract'] = user.get_total_contributions_activies_contract()
        context['avarage_percent_activies_contract'] = user.get_avarage_percent_activies_contract()
        context['total_dividends_received'] = user.get_total_dividends_received()
        context['percent_invest'] = user.get_percent_invest()


        return context
    

class SupportView(TemplateView):
    template_name = 'dashboard/support.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


dashboard_view = DashboardView.as_view()
support_view = SupportView.as_view()
