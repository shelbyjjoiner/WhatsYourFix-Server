from django.db import models
from django.contrib.auth.models import User

class NeuroUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'neuro_user' )
    bio = models.CharField(max_length=100)
    hobby = models.ManyToManyField("Hobbies")