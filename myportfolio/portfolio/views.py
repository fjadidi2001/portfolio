# portfolio/views.py

from django.shortcuts import render
from .models import Project, Skill, Experience


def portfolio_view(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'portfolio/portfolio.html', {
        'projects': projects,
        'skills': skills,
        'experiences': experiences,
    })
