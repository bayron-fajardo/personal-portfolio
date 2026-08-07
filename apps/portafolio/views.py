from django.views import View
from django.shortcuts import render
from apps.proyectos.models import Project

class HomeView(View):
    
    def get(self, request):
        
        projects = Project.objects.all()
        context = {
            "projects" : projects,
        }
        return render(request, 'home.html', context)
