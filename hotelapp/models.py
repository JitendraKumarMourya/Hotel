from os import times
from django.core.exceptions import RequestAborted
from django.db import models

# Create your models here.

# for user room BOOK
class hotelappAdmin(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    address=models.CharField(max_length=50)
    profile=models.ImageField()
    dob=models.CharField(max_length=100)


class bookRoom(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Email=models.CharField(max_length=40)
    Mobile=models.CharField(max_length=12)
    Address=models.CharField(max_length=50)
    City=models.CharField(max_length=30)
    State=models.CharField(max_length=30)
    CheckInDate=models.DateField()
    CheckInTime=models.TimeField()
    CheckOutDate=models.DateField()
    CheckOutTime=models.TimeField()
    RoomType=models.CharField(max_length=50)
    Adults=models.IntegerField()
    Childrens=models.IntegerField()
    IdType=models.CharField(max_length=25)


# hotel details
class hoteldetails(models.Model):
    hotelimage=models.ImageField()
    hotelname=models.CharField(max_length=200)
    hoteldescription=models.CharField(max_length=300)
    hotellocation=models.CharField(max_length=100)


# room Type 
class roomType(models.Model):
    roomType=models.CharField(max_length=150)
    roomPrice=models.IntegerField(default=0)
    status=models.BooleanField(default=True)
    hotelId=models.ForeignKey('addHotels', on_delete=models.CASCADE)

# Add new Hotes Models
class addHotels(models.Model):
    hotelimage=models.ImageField()
    hotelname=models.CharField(max_length=50)
    hoteldescription=models.CharField(max_length=100)
    hotellocation=models.CharField(max_length=100)










    

    

