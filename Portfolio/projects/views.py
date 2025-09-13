from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Project
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Project


# def project(request):
#     projects = Project.objects.all()
#     context = {'projects': projects}
#     return render(request, 'projects/projects.html', context)

# projects/views.py

def project(request):
    projects = Project.objects.all()
    
    # Crée un objet Paginator avec 4 projets par page
    paginator = Paginator(projects, 4) 
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {'page_obj': page_obj}
    return render(request, 'projects/projects.html', context)

def project_detail_view(request, project_id):
    # Utilise get_object_or_404 pour récupérer le projet par son ID ou renvoyer une erreur 404
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})