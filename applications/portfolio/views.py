from django.shortcuts import render
from .models import Project
# Create your views here.

def home(request):
    projects = Project.objects.all().order_by('pk')
    return render(request, 'portfolio/home.html',{'projects':projects})