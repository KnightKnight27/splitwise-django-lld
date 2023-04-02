from django.db import models
from .BaseModel import BaseModel


class Transaction(BaseModel):
    sender = models.ForeignKey(to='User')
    receiver = models.ForeignKey(to='User')
    amount = models.FloatField()