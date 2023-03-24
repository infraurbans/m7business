from django.db import models
from django.db.models import Count, F, Sum, Avg

class ContractQuerySet(models.QuerySet):
    def activies(self):
        queryset = self.annotate(
            total_dividends=Count('dividend__pk', distinct=True)
        ).filter(
            duration__gt=F('total_dividends')
        ).distinct()

        return queryset
    
    def total_contribution(self):
        return self.aggregate(total_sum=Sum('contribution')).get('total_sum', 0)
    
    def avarage_percent(self):
        return self.aggregate(avarage_percent=Avg('percent')).get('avarage_percent', 0)


ContractManager = models.Manager.from_queryset(ContractQuerySet)
