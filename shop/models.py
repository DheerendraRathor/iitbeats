from django.db import models
from django.contrib.auth.models import User


class Shop(models.Model):
    name = models.CharField(max_length=256)
    status = models.BooleanField(default=True)
    address = models.TextField()
    phone = models.CharField(max_length=32)
    user = models.ForeignKey(User)