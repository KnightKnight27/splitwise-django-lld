from django.db import models
from .BaseModel import BaseModel
from .User import User


class Group(BaseModel):
    name = models.CharField(max_length=255)
    # GROUP : USERS
    #   M    :  M -> MANY TO MANY RELATIONSHIP

    # EACH GROUP WILL HAVE EXPENSES
    # ONE GROUP CAN HAVE MULTIPLE EXPENSE
    # AN EXPENSE CAN NOT BELONG TO MULTIPLE GROUPS
    # ONE TO MANY RELATIONSHIP -> IN EXPENSE U CAN JUST WRITE GROUP
    # WE ARE SUPPOSED TO HAVE A THIRD TABLE

    participants = models.ManyToManyField(User, related_name="group_participants")
    admins = models.ManyToManyField(User,related_name="group_admins")
    # 1 to M relationship with expenses
    description = models.CharField(max_length=255,default=" ")