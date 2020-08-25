from django.shortcuts import render, get_object_or_404
from .models import Job

def home(request):
    #get all the jobs from the database
    jobs = Job.objects
    return render(request,'jobs/home.html', {'jobs': jobs})


def jdetail(request, job_id):
    #get specific job id from the database
    detailjob= get_object_or_404(Job, pk=job_id)
    return render (request,'jobs/jdetail.html',{'job': detailjob})