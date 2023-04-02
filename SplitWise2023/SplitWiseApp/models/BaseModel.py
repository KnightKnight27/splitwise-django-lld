from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
