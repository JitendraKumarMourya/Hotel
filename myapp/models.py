from django.db import models

# Create your models here.

class adminRegistration(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email_mobile=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    dob=models.DateField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    file=models.CharField(max_length=150)
    

