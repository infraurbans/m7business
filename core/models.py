from django.db import models

# Create your models here.

#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Contrato(models.Model):
    usuario = models.ForeignKey(get_user_model(), verbose_name='Cliente', on_delete=models.CASCADE)
    Aporte = models.FloatField()
    prazo = models.IntegerField('Duração em meses')
    pagamento_choices = [
        (1, '01'),
        (5, '05'),
        (10, '10'),
        (15, '15'),
        (20, '20'),
        (25, '25'),
    ]
    pagamento = models.CharField(
        max_length=2,
        choices=pagamento_choices,
        default=1,
    )

class Dividendo(models.Model):
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    valor = models.FloatField('Valor do contrato')
    data = models.DateField()
    comprovante = models.FileField(upload_to='uploads/%Y/%m/%d/')
    ordem = models.CharField('Sequencial', max_length=5)
      