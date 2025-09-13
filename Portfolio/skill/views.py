from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Experience
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from wsgiref.util import FileWrapper


def skill(request):
    # Récupérer toutes les expériences triées par année décroissante
    experiences = Experience.objects.all().order_by('-date')

    # Pagination : 4 expériences par page
    paginator = Paginator(experiences, 4)
    page_number = request.GET.get('page')  # Récupérer le numéro de page depuis l'URL
    page_obj = paginator.get_page(page_number)  # Obtenir les objets de la page actuelle

    return render(request, 'skill/skill.html', {'page_obj': page_obj})


# def view_certification(request, experience_id):
#     """
#     Cette vue sert le fichier de certification en ligne.
#     Elle empêche le téléchargement en définissant le bon type MIME.
#     """
#     experience = get_object_or_404(Experience, pk=experience_id)
    
#     # Assurez-vous que le fichier existe avant d'essayer de le lire
#     if experience.certification_file:
#         # file_path = experience.certification_file.path
        
#         # with open(file_path, 'rb') as f:
#         #     file_data = f.read()

#         # # Déterminer le type MIME pour l'affichage dans le navigateur
#         # # Pour un PDF, le type est 'application/pdf'
#         # # Pour une image, le type serait 'image/jpeg', 'image/png', etc.
#         # # Vous pouvez utiliser le module 'mimetypes' si vous avez différents types de fichiers
        
#         # mime_type = 'application/pdf' # Exemple pour un PDF
        
#         # response = HttpResponse(file_data, content_type=mime_type)
        
#         # # Le contenu est affiché en ligne. L'en-tête 'Content-Disposition' n'est pas nécessaire, 
#         # # mais si vous voulez être explicite, utilisez 'inline' au lieu de 'attachment'.
#         # response['Content-Disposition'] = f'inline; filename="{experience.certification_file.name}"'
        
#         # return response
    
#         #experience = get_object_or_404(Experience, pk=experience_id)
#         file_path = experience.certification_file.path

#         # Ouvre le fichier en mode binaire
#         file = open(file_path, 'rb')
#         response = HttpResponse(FileWrapper(file), content_type='application/pdf')

#         # Ceci est la ligne clé qui empêche le téléchargement par défaut
#         response['Content-Disposition'] = 'inline; filename="%s"' % experience.certification_file.name
#         return response

#     else:
#         return HttpResponse("Fichier non trouvé.", status=404)


# from django.http import FileResponse, HttpResponseForbidden, Http404
# from django.shortcuts import get_object_or_404
# from .models import Experience
# import mimetypes
# import os

# def view_certification(request, pk):
#     """
#     Affiche la certification dans un iframe sans proposer le téléchargement direct.
#     """
#     experience = get_object_or_404(Experience, pk=pk)

#     if not experience.certification_file:
#         return HttpResponseForbidden("Aucun fichier de certification disponible.")

#     file_path = experience.certification_file.path

#     if not os.path.exists(file_path):
#         raise Http404("Fichier introuvable")

#     file_type, _ = mimetypes.guess_type(file_path)

#     response = FileResponse(open(file_path, 'rb'), content_type=file_type)
#     response['Content-Disposition'] = 'inline'  # Affichage direct (pas download)
#     return response

from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from .models import Experience # Assurez-vous que l'importation de votre modèle est correcte
import os # Importez le module os

def show_certification(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    file_path = experience.certification_file.path
    
    # Vérifiez si le fichier existe
    if not os.path.exists(file_path):
        return HttpResponse("Fichier non trouvé.", status=404)
    
    file_wrapper = FileWrapper(open(file_path, 'rb'))
    
    # Détecter le type de contenu (MIME type)
    # Ceci est important pour que le navigateur sache comment afficher le fichier
    mime_type = 'application/pdf' # Pour les PDF
    if file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
        mime_type = 'image/jpeg'
    elif file_path.endswith('.png'):
        mime_type = 'image/png'
    # Ajoutez d'autres types de fichiers si nécessaire
    
    response = HttpResponse(file_wrapper, content_type=mime_type)
    
    # L'en-tête 'inline' indique au navigateur d'afficher le contenu.
    response['Content-Disposition'] = 'inline; filename="%s"' % os.path.basename(file_path)
    
    return response



from django.views.static import serve
from django.conf import settings
from django.http import Http404

def protected_serve(request, path):
    # Vérifier si le fichier demandé est un certificat
    if path.startswith('certificats/'):
        # Vérifier que la requête provient de votre site
        referer = request.META.get('HTTP_REFERER', '')
        if not referer.startswith(settings.SITE_URL):
            raise Http404("Fichier non trouvé")
        
        # Servir le fichier avec des en-têtes de sécurité
        response = serve(request, path, document_root=settings.MEDIA_ROOT)
        response['X-Frame-Options'] = 'SAMEORIGIN'
        response['Content-Disposition'] = 'inline'
        return response
    else:
        return serve(request, path, document_root=settings.MEDIA_ROOT)



# views.py
from django.http import FileResponse, Http404
from django.conf import settings
import os

# def view_certificate(request, filename):
#     path = os.path.join(settings.MEDIA_ROOT, filename)
#     if os.path.exists(path):
#         response = FileResponse(open(path, 'rb'), content_type='application/pdf')
#         response['X-Frame-Options'] = 'SAMEORIGIN'  # permet l'affichage dans iframe
#         return response
#     else:
#         raise Http404("Fichier non trouvé")


from django.views.static import serve
from django.conf import settings
from django.http import Http404
import os

def protected_serve(request, path):
    # Vérifier si le fichier demandé est un certificat
    if path.startswith('certificats/'):
        # Vérifier que la requête provient de votre site
        referer = request.META.get('HTTP_REFERER', '')
        if not referer.startswith(settings.SITE_URL):
            raise Http404("Fichier non trouvé")
        
        # Servir le fichier avec des en-têtes de sécurité
        response = serve(request, path, document_root=settings.MEDIA_ROOT)
        response['X-Frame-Options'] = 'SAMEORIGIN'
        response['Content-Disposition'] = 'inline'
        response['X-Content-Type-Options'] = 'nosniff'
        return response
    else:
        return serve(request, path, document_root=settings.MEDIA_ROOT)





import os
from django.http import HttpResponse, Http404
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

import tempfile
from pdf2image import convert_from_path
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import io
from PIL import Image

@require_GET
@xframe_options_sameorigin
def serve_certificate(request, certificate_path):
    # Vérifier que le chemin est sécurisé
    if not certificate_path or '..' in certificate_path:
        raise Http404("Certificat non trouvé")
    
    # Chemin complet du fichier
    file_path = os.path.join(settings.MEDIA_ROOT, certificate_path)
    
    # Vérifier que le fichier existe et est dans le dossier des certificats
    if not os.path.exists(file_path) or not file_path.startswith(os.path.join(settings.MEDIA_ROOT, 'certificats')):
        raise Http404("Certificat non trouvé")
    
    # Déterminer le type MIME en fonction de l'extension
    ext = os.path.splitext(file_path)[1].lower()
    mime_types = {
        '.pdf': 'application/pdf',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.gif': 'image/gif',
    }
    content_type = mime_types.get(ext, 'application/octet-stream')
    if ext == '.pdf':
        try:
            # Convertir la première page du PDF en image
            images = convert_from_path(file_path, first_page=1, last_page=1, dpi=150)
            if images:
                # Convertir l'image en bytes
                img_io = io.BytesIO()
                images[0].save(img_io, format='JPEG', quality=85)
                img_io.seek(0)
                
                response = HttpResponse(img_io.getvalue(), content_type='image/jpeg')
                response['Content-Disposition'] = 'inline'
                return response
            else:
                raise Http404("Impossible de convertir le PDF")
        except Exception as e:
            raise Http404(f"Erreur de conversion: {str(e)}")
    else:
        # Pour les images normales
        try:
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type=content_type)
                response['Content-Disposition'] = 'inline'
                response['X-Content-Type-Options'] = 'nosniff'
                return response
        except IOError:
            raise Http404("Erreur de lecture du certificat")
        
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.http import require_GET
from .models import Experience
import os

def skill_view(request):
    experiences_list = Experience.objects.all().order_by('-date')
    paginator = Paginator(experiences_list, 6)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'skill/skill.html', {'page_obj': page_obj})

@require_GET
@xframe_options_sameorigin
def serve_protected_file(request, file_path):
    """
    Vue pour servir les fichiers de manière sécurisée
    """
    # Vérifications de sécurité
    if not file_path or '..' in file_path:
        raise Http404("Fichier non trouvé")
    
    # Chemin complet du fichier
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    
    # Vérifier que le fichier existe
    if not os.path.exists(full_path):
        raise Http404("Fichier non trouvé")
    
    # Vérifier que le fichier est dans le dossier des certificats
    if not full_path.startswith(os.path.join(settings.MEDIA_ROOT, 'certificats')):
        raise Http404("Fichier non autorisé")
    
    # Déterminer le type MIME
    content_type = 'application/octet-stream'
    if file_path.endswith('.pdf'):
        content_type = 'application/pdf'
    elif file_path.endswith(('.jpg', '.jpeg')):
        content_type = 'image/jpeg'
    elif file_path.endswith('.png'):
        content_type = 'image/png'
    elif file_path.endswith('.gif'):
        content_type = 'image/gif'
    
    # Lire et servir le fichier
    try:
        with open(full_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type=content_type)
            # Empêcher le téléchargement
            response['Content-Disposition'] = 'inline'
            response['X-Content-Type-Options'] = 'nosniff'
            return response
    except IOError:
        raise Http404("Erreur de lecture du fichier")
    
import mimetypes
import os
from django.http import HttpResponse, Http404
from django.conf import settings

def view_certificate(request, filename):
    # chemin absolu du fichier
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    if not os.path.exists(file_path):
        raise Http404("Certificat introuvable")

    # détection du type mime (ex: application/pdf, image/png…)
    mime_type, _ = mimetypes.guess_type(file_path)

    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type=mime_type or 'application/octet-stream')

        # ATTENTION : inline = affichage dans le navigateur (pas de téléchargement)
        response['Content-Disposition'] = f'inline; filename="{os.path.basename(file_path)}"'
        return response


'''
{% extends 'base.html' %}
{% load static %}

{% block content %}
<link rel="stylesheet" href="{% static 'skill/css/skill.css' %}">
<div class="skills-container">
    <h2>Mes Expériences et Certifications</h2>

    <!-- Grille des expériences (2x2) -->
    <div class="skills-grid">
        {% for experience in page_obj %}
        <div class="experience-card">
            <h3>{{ experience.title }}</h3>
            <p class="organization">{{ experience.organization }} - {{ experience.year }}</p>
            <p class="description">{{ experience.description }}</p>
            {% if experience.certification_file %}
            <a href="{{ experience.certification_file.url }}" target="_blank" class="certification-link" download>Voir la certification</a>
            {% endif %}
        </div>
        {% endfor %}
    </div>

    <!-- Pagination -->
    <div class="pagination">
        <span class="step-links">
            {% if page_obj.has_previous %}
                <a href="?page=1" class="pagination-link">&laquo; Première</a>
                <a href="?page={{ page_obj.previous_page_number }}" class="pagination-link">Précédente</a>
            {% endif %}

            <span class="current">
                Page {{ page_obj.number }} sur {{ page_obj.paginator.num_pages }}.
            </span>

            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}" class="pagination-link">Suivante</a>
                <a href="?page={{ page_obj.paginator.num_pages }}" class="pagination-link">Dernière &raquo;</a>
            {% endif %}
        </span>
    </div>
</div>
{% endblock %}
'''

