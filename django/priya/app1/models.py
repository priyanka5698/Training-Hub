from django.db import models

# Create your models here.
class Regform1(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


def __str__(self):
    return self.firstname
