from distutils.command.upload import upload
from django.db import models

# Create your models here.
class PostData(models.Model):
    name = models.CharField(max_length=100)
    discription = models.TextField()
    image = models.ImageField(upload_to ='images')