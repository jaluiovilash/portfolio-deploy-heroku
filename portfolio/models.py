from django.db import models
from django.db.models.base import Model

# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=25)
    description=models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.username
    

class Blogs(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField()
    authName=models.CharField( max_length=15)
    img=models.ImageField(upload_to='blog', blank=True, null=True)
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title