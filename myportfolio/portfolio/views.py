# portfolio/views.py

from django.shortcuts import render
from .models import Academic_References


def portfolio_view(request):
    projects = Academic_References.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})
