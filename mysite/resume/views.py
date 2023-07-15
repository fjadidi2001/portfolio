from django.shortcuts import render
from .models import Resume


def resume(request):
    resu1me = Resume.objects.get(id=1)
    context = {
        'resume': resu1me,
    }
    return render(request, 'resume.html', context)
