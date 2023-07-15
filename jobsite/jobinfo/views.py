from django.shortcuts import render
from .models import JobApplication


def job_list(request):
    applications = JobApplication.objects.all()
    return render(request, 'jobinfo/job_list.html', {'applications': applications})
