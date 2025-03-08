from django.db import models
from AdminPanel.models import Player


class EndUser(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    budget = models.IntegerField(default=9000000)
    players = models.ManyToManyField(Player)
    type = models.CharField(max_length=100, default='user', choices=[('user', 'User'), ('admin', 'Admin')])

class Token(models.Model):
    token = models.CharField(max_length=100)
    user = models.ForeignKey(EndUser, on_delete=models.CASCADE)