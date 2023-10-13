from django.db import models
from django.contrib.auth.models import AbstractUser

class Color(models.Model):
    value = models.CharField(max_length=6)

class User(AbstractUser):
    friends = models.ManyToManyField('self', symmetrical=True)
    isPrivate = models.BooleanField(default=False)
    askBeforeStick = models.BooleanField(default=False)
    boardColor = models.ForeignKey(Color, on_delete=models.CASCADE, default=None, null=True)
    stickersOnBoard = models.ManyToManyField('Sticker')

class Sticker(models.Model):
    content = models.TextField(max_length=150)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)