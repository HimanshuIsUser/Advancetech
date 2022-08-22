from pyexpat import model
from sqlite3 import Timestamp
from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    Timestamp = models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message form ' + self.name + '- ' + self.email
