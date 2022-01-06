from django.shortcuts import render, get_list_or_404
from .models import job
# Create your views here.
def home(request):
    jobs = job.objects
    return render(request, 'job/home.html', {'jobs': jobs})

def detail(request, job_id):
    job_detail = get_list_or_404(job, pk=job_id)

    return render(request, 'job/detail.html', {'job':job_detail})


    