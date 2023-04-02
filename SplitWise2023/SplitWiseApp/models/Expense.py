from django.db import models
from .BaseModel import BaseModel
from .User import User
from .Group import Group

class Expense(BaseModel):
    amount = models.IntegerField()
    group =  models.ForeignKey(Group, on_delete=models.PROTECT)
    #  expense : user
    #    M     : 1
    expense_created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    participants = models.ManyToManyField(User,related_name="expense_participants")