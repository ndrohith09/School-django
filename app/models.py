from django.core.mail import mail_managers
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Gallery(models.Model):
    Image = models.ImageField(upload_to = 'photos/')



GENDER_CHOICES = (
    ("1","Male"),
    ("2","Female"),
    ("3","Prefer not to say"),
)

class Admission(models.Model):
    fullname = models.TextField(max_length=100)
    username = models.TextField(max_length=100)
    email = models.EmailField()
    phonenumber =models.PositiveIntegerField(max_length=10)
    password1 = models.TextField(max_length=100)
    password2 = models.TextField(max_length=100)
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES,default='3')
    