from django.shortcuts import render
from models import Resume
def resume(request):
    resume = Resume.objects.get(id=1)
    context = {
        'resume': resume,
    }
    return render(request, 'resume.html', context)
