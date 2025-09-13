from django.shortcuts import render
from .models import About

# Create your views here.
# def about(request):

#     return render(request, 'about/about.html')


# def about(request):
#     about = About.objects.first()  # Récupère la première entrée (s'il y en a une)
#     return render(request, 'about/about.html', {'about': about})


from django.shortcuts import render, get_object_or_404
from .models import AboutMe

def about(request):
    about = AboutMe.objects.first()  # retourne None si aucun objet
    context = {
        'about': about
    }
    return render(request, 'about/about.html', context)
