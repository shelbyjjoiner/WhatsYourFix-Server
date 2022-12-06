from django.db import models

class UserHobbies(models.Model):
    neuro_user= models.ForeignKey("NeuroUser", on_delete=models.CASCADE)
    hobbie = models.ForeignKey("Hobbies", on_delete=models.CASCADE, related_name='hobbyists')