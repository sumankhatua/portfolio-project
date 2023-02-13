from django.shortcuts import render
# import jobs from the database to show in the website front-end
from .models import Job
# Create your views here.

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})
