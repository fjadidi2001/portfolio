from django.urls import path

from mysite.resume.views import resume

urlpatterns = [
    path('resume/', resume),
]
