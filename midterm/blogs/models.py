from django.db import models

# Create your models here.



class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    owner = models.CharField(max_length=255)

def __str__(self):
    return self.title