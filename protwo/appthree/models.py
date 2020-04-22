from django.db import models

# Create your models here.

class User(models.Model):
    Firstname = models.CharField(max_length= 128)
    Lastname = models.CharField(max_length= 128)
    Email = models.EmailField(max_length= 264,unique=True)

    def __str__(self):
        return self.Firstname
