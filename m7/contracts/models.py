from django.db import models
from django.contrib.auth import get_user_model

from m7.core.models import BaseModel

class Contract(BaseModel):
    user = models.ForeignKey(get_user_model(), verbose_name='Cliente', on_delete=models.CASCADE)
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
    payment = models.CharField(max_length=2, choices=PAYMENT_CHOICES, default=DAY_1)
