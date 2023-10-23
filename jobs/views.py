from django.shortcuts import render
from django.views import generic
from .models import Job, Company, Category

class JobList(generic.ListView):
    model=Job
# Create your views here.

class JobDetail(generic.DetailView):
    model=Job