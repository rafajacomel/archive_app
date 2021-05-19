from django.contrib.auth.models import User
from django.db import models


class Fix(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    fspId = models.CharField(max_length=8)
    name = models.TextField(max_length=32)
    path = models.TextField(max_length=32)
    status = models.TextField(max_length=16)
    number_of_last_download = models.IntegerField()
    number_of_users = models.IntegerField()
