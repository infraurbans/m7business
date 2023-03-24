from django.db import models

from m7.core.models import BaseModel
from m7.contracts.models import Contract

from m7.dividends.managers import DividendManager

class Dividend(BaseModel):
    payment_date = models.DateField()
    receipt = models.FileField(upload_to='recibos/%Y/%m/%d/')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    value = models.DecimalField('Valor pago', decimal_places=2, max_digits=9)
    order = models.SmallIntegerField('Sequencial')

    objects = DividendManager()

    def __str__(self):
        return f'{self.contract.user} - {self.payment_date}'
    
    class Meta:
        verbose_name="Dividendo"
        verbose_name_plural = "Dividendos"
        ordering = ('-payment_date', )
