import datetime
from django.db import models
from dateutil.relativedelta import relativedelta
from m7.core.models import BaseModel
from m7.contracts.managers import ContractManager
from django.db.models import Sum

class Contract(BaseModel):
    user = models.ForeignKey('accounts.User', verbose_name='Cliente', on_delete=models.CASCADE)
    contribution = models.FloatField("Investimento inicial")
    duration = models.IntegerField('Duração em meses')
    PAYMENT_CHOICES = [(day, f'Dia {day}') for day in range(1, 31)]
    payment_day = models.SmallIntegerField("Dia de pagamento", choices=PAYMENT_CHOICES, default=1)
    percent = models.DecimalField("Porcentagem", decimal_places=2, max_digits=5)
    contract_file = models.FileField(upload_to='cotratos/%Y/%m/%d/', null=True, blank=True)
    start_at = models.DateField("Início do contrato")

    objects = ContractManager()

    def __str__(self):
        return f'{self.user} | {self.start_at}'

    @property
    def is_active(self):
        return self.duration > self.count_dividends

    @property
    def count_dividends(self):
        return self.dividend_set.all().count()
    
    @property
    def total_paid(self):
        return self.dividend_set.all().aggregate(
            total_paid=Sum('value')
        ).get('total_paid', 0)
    
    @property
    def expected_end(self):
        return self.start_at + relativedelta(months=self.duration)
    
    class Meta:
        verbose_name="Contrato"
        ordering = ('-start_at', )
