from django.db import models 

class Comments(models.Model): 
    body = models.CharField(max_length=100)