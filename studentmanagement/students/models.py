from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=100)
    course=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    image=models.ImageField(upload_to='student_images')