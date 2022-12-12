from django.db import models
from django.contrib.auth.models import User

class NeuroUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'neuro_user' )
    bio = models.CharField(max_length=100)
    hobbies = models.ManyToManyField("Hobbies")

    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}' 