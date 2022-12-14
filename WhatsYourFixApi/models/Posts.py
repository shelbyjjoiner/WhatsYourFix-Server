from django.db import models 

class Posts(models.Model): 
    user = models.ForeignKey("NeuroUser", on_delete=models.CASCADE, related_name='posts')
    hobbies = models.ForeignKey("Hobbies", on_delete=models.CASCADE, related_name='hobbie')
    body = models.CharField(max_length=250)
    image = models.ImageField()
    item = models.CharField(max_length=25)
 