from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Registrations(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class ProfileData(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)

class TeacherData(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(max_length=200)

class UploadImage(models.Model):
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

class Newdata(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(Registrations,on_delete=models.CASCADE)

class Newdata1(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
