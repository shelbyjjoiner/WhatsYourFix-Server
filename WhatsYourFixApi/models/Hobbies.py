from django.db import models

class Hobbies(models.Model):
    label = models.CharField(max_length=50)