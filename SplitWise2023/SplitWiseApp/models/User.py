from django.db import models
from .BaseModel import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    hashed_password = models.CharField(max_length=255)