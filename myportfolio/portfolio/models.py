# portfolio/models.py

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add more fields like project image, URL, etc.


class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Add more fields like duration, company name, etc.
