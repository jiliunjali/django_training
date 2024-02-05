from django.db import models
from django.contrib.auth.models import User #it is for being able to use superuser and users
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.title + '|' + str(self.author)  # doing this enable us see entries in post as string rather than just objects 
