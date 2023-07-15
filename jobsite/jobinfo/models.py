from django.db import models


class JobApplication(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    date_applied = models.DateField(auto_now_add=True)
