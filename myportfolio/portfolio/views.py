# portfolio/views.py

from django.shortcuts import render
from .models import Summary, Education, WorkExperience, Skills, Project, AcademicReferences, ProfessionalReferences


def portfolio_view(request):
    summary = Summary.objects.all()
    education = Education.objects.all()
    workExperience = WorkExperience.objects.all()
    skills = Skills.objects.all()
    project = Project.objects.all()
    academicReferences = AcademicReferences.objects.all()
    professionalReferences = ProfessionalReferences.objects.all()
    return render(request, 'portfolio/portfolio.html', {
        'summary': summary,
        'education': education,
        'workExperience': workExperience,
        'skills': skills,
        'project': project,
        'academicReferences': academicReferences,
        'professionalReferences': professionalReferences,
    })
