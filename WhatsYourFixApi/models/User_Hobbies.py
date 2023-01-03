from django.db import models

class UserHobbies(models.Model):
    user= models.ForeignKey("NeuroUser", on_delete=models.CASCADE)
    hobby= models.ForeignKey("Hobbies", on_delete=models.CASCADE, related_name='hobbyists')