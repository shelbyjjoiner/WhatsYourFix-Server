from django.db import models 

class Comments(models.Model): 
    user = models.ForeignKey("NeuroUser", on_delete=models.CASCADE, related_name="comments")    
    post = models.ForeignKey("Posts", on_delete=models.CASCADE, related_name="post_comments")
    body = models.CharField(max_length=100)
