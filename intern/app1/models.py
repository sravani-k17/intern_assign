from django.db import models
from phone_field import PhoneField

class Student(models.Model):

	Student_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=150)
	email = models.EmailField(max_length=254)
	phone = PhoneField(blank=True, help_text='Contact phone number')
	profile_pic = models.ImageField(upload_to = 'images/')
	video = models.FileField(upload_to = 'videos/',default='media/images/d1.jpg')
	branch = models.CharField(max_length=10,default='ece')


# Create your models here.
