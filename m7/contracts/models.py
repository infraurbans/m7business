from django.db import models
from dateutil.relativedelta import relativedelta

from m7.core.models import BaseModel
from m7.contracts.managers import ContractManager

class Contract(BaseModel):
    user = models.ForeignKey('accounts.User', verbose_name='Cliente', on_delete=models.CASCADE)
    contribution = models.FloatField()
    duration = models.IntegerField('Duração em meses')
    DAY_1, DAY_5, DAY_10, DAY_15, DAY_20, DAY_25 = 1, 5, 10, 15, 20, 25
    PAYMENT_CHOICES = [
        (DAY_1, '01'),
        (DAY_5, '05'),
        (DAY_10, '10'),
        (DAY_15, '15'),
        (DAY_20, '20'),
        (DAY_25, '25'),
    ]
    payment_day = models.SmallIntegerField("Dia de pagamento", choices=PAYMENT_CHOICES, default=DAY_1)
    percent = models.DecimalField("Porcentagem", decimal_places=2, max_digits=5)
    contract_file = models.FileField(upload_to='cotratos/%Y/%m/%d/', null=True, blank=True)

    objects = ContractManager()

    @property
    def is_active(self):
        return self.duration > self.count_dividends

    @property
    def count_dividends(self):
        return self.dividend_set.all().count()
    
    @property
    def expected_end(self):
        return self.created_at + relativedelta(months=self.duration)
