# portfolio/models.py

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    # Add more fields as needed
