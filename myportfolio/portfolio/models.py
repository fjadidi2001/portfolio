# this is my model
from django.db import models


class Summary(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Education(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class WorkExperience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Skills(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class AcademicReferences(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class ProfessionalReferences(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
