from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    friends = models.ManyToManyField('self', symmetrical=True, blank=True)
    isPrivate = models.BooleanField(default=False)
    askBeforeStick = models.BooleanField(default=False)
    stickersOnBoard = models.ManyToManyField('Sticker', blank=True)

class Sticker(models.Model):
    content = models.TextField(max_length=150)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)