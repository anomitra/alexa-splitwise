from django.db import models
from core.models import BaseModel


class Transaction(BaseModel):
    USER_GT = 'GT'
    USER_ANO = 'Ano'

    USER_CHOICES = (
        (USER_GT, 'GT'),
        (USER_ANO, 'Ano'),
    )

    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=200)
    user = models.CharField(max_length=10, choices=USER_CHOICES)
