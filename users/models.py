from pyexpat import model
from statistics import mode
from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    type = models.CharField(max_length=10)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    confirm_password = models.CharField(max_length=30)
    line1 = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.CharField(max_length=30)
    profilepicture = models.ImageField(upload_to='images')  

class Blog(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=250)
    category = models.CharField(max_length=30)
    content = models.CharField(max_length=10000000)
    image = models.ImageField(upload_to='blogs')
    isdraft = models.IntegerField()
    user = models.CharField(max_length=20)