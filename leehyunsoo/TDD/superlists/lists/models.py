# from django.db.models import Model as DjangoModel, ForeignKey
from django.db import models


#
# class BaseModel(DjangoModel):
#     class Meta:
#         abstract = True
#

class List(models.Model):
    pass


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=True)
