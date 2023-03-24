from django.db import models
from m7.contracts.models import Contract
from m7.core.models import BaseModel


class Dividend(BaseModel):
    date = models.DateField()
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    value = models.FloatField('Valor do Contrato')
    receipt = models.FileField(upload_to='uploads/%Y/%m/%d/')
    order = models.CharField('Sequencial', max_length=5)
