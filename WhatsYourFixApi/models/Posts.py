from django.db import models 

class Posts(models.Model): 
    user = models.ForeignKey("NeuroUser", on_delete=models.CASCADE, related_name='neuro')
    hobbies = models.ForeignKey("Hobbies", on_delete=models.CASCADE, related_name='hobbie')
    content = models.CharField(max_length=250)
    image = models.ImageField()
    item = models.CharField(max_length=25)
 