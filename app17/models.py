from django.db import models

# Create your models here.

class StudentDetails(models.Model):
    number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    photo = models.ImageField(upload_to='student_images')
    email = models.EmailField(max_length=30)
    date_of_regi = models.DateField(auto_now_add=True)
