from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()

    def __str__(self):
        return self.name
