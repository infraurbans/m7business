from django.db import models
from django.db.models import Count, F, Sum, Avg


class DividendQuerySet(models.QuerySet):
    def total_received(self):
        return self.aggregate(
            total_received=Sum('value')
        ).get('total_received', 0)


DividendManager = models.Manager.from_queryset(DividendQuerySet)
