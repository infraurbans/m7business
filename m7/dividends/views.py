from django.shortcuts import render
from django.views.generic.list import ListView

from m7.dividends.models import Dividend


class MyDividends(ListView):
    model = Dividend
    paginate_by = 100
    template_name = "dashboard/dividends/my_dividends.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


my_dividends = MyDividends.as_view()
