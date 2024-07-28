from django.db import models

# Create your models here.
class Contact(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    number=models.CharField(max_length=10)
    description=models.TextField(max_length=250)

    def __str__(self) -> str:
        return self.username