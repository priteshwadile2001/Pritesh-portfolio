from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.name
    
from django.db import models


    


class Blogs(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    authname = models.CharField(max_length=50)
    img =models.ImageField(upload_to='blog',blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title