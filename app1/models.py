# models.py
from django.db import models

class UploadedImage(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    is_forgery = models.BooleanField(default=False)  # Add this line for forgery detection

