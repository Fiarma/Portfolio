from django.urls import path
from . import views
from django.urls import re_path
from .views import view_certificate

urlpatterns = [
    path('', views.skill, name='skill'),
   # path('certification/<int:experience_id>/', views.view_certification, name='view_certification'),
    path('certification/<int:experience_id>/', views.show_certification, name='show_certification'),

    re_path(r'^media/(?P<path>.*)$', views.protected_serve),
    path('certificate/<str:filename>/', view_certificate, name='view_certificate'),
    re_path(r'^media/(?P<path>.*)$', views.protected_serve),

    path('certificat/<path:certificate_path>', views.serve_certificate, name='serve_certificate'),
    path('fichier-protege/<path:file_path>', views.serve_protected_file, name='serve_protected_file'),
    path('skill/certificate/<path:filename>/', views.view_certificate, name='view_certificate'),


]

from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Remplacez la ligne static pour utiliser la vue protégée
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', views.protected_serve),
    ]

'''

/* Styles pour le corps de la page */
body {
    font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f7f9;
    color: #333;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* Styles pour les boutons de navigation */
.navigation-buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;
    margin-top: 20px;
    margin-bottom: 40px;
    position: absolute;
    top: 80px;
    left: 0;
    right: 0;
}

.nav-button {
    display: flex;
    align-items: center;
    gap: 5px;
    padding: 12px 24px;
    background-color: transparent;
    color: rgb(50, 80, 179);
    text-decoration: none;
    font-weight: bold;
    border: 2px solid rgb(50, 80, 179);
    border-radius: 5px;
    transition: background-color 0.3s ease, color 0.3s ease;
}

.nav-button:hover {
    background-color: rgb(50, 80, 179);
    color: white;
}

/* Style pour les flèches */
.button-arrow {
    font-size: 1.2rem;
    line-height: 1;
}

/* Conteneur principal */
.education-container {
    max-width: 1000px;
    margin: 50px auto;
    padding: 20px;
    background-color: transparent;
}

/* Titre principal */
.education-container h2 {
    text-align: center;
    margin-bottom: 30px;
    color: #333;
    margin-top: 100px;
}

/* Grille des expériences */
.education-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr); /* CORRIGÉ: Force 2 colonnes sur les grands écrans */
    gap: 20px;
}

/* Carte expérience */
.education-card {
    background: #ffffff;
    padding: 3rem;
    border-radius: 12px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    border-left: 5px solid rgb(50, 80, 179);
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    display: flex;
    flex-direction: column;
}

/* Effet de survol sur la carte */
.education-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
}

/* Alignement numéro + titre */
.education-header {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}

/* Numéro circulaire */
.education-number {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: rgb(50, 80, 179);
    color: white;
    font-size: 1.2rem;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

/* Titre expérience */
.education-degree {
    color: rgb(50, 80, 179);
    font-weight: bold;
    font-size: 1.2rem;
    margin: 0;
}

/* Ligne d'information (Organisation et Date) */
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    padding: 5px 0;
}

/* Label d'information */
.info-label {
    font-weight: 700;
    color: #bbb;
    font-size: 1rem;
}

/* Valeur d'information */
.info-value {
    font-weight: 600;
    color: #333;
    font-size: 1rem;
}

/* Valeur de date */
.date-value {
    color: #333;
    font-weight: bold;
}

/* Description */
.education-description {
    font-size: 1rem;
    color: #555;
    line-height: 1.6;
    margin: 15px 0;
    padding-top: 10px;
    border-top: 1px solid #eee;
    flex-grow: 1;
}

/* Lien de certification */
.certification-link {
    display: inline-block;
    padding: 10px 20px;
    background-color: transparent;
    color: rgb(50, 80, 179);
    text-decoration: none;
    font-weight: bold;
    border: 2px solid rgb(50, 80, 179);
    border-radius: 5px;
    transition: background-color 0.3s ease, color 0.3s ease;
    margin-top: 15px;
    align-self: flex-start;
}

.certification-link:hover {
    background-color: rgb(50, 80, 179);
    color: white;
}

/* Pagination */
/* Pagination */
.pagination {
    margin-top: 40px;
    margin-bottom: 50px;
    text-align: center;
    width: 100%;
}

.pagination .step-links {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap; /* évite le débordement */
    gap: 10px;
}

.pagination-link,
.pagination .current {
    display: inline-block;
    padding: 8px 16px;
    margin: 0;
    border-radius: 5px;
    font-weight: bold;
    text-decoration: none;
    transition: background-color 0.3s, color 0.3s;
    white-space: nowrap; /* empêche les retours à la ligne dans le texte */
}

/* Boutons pagination (normal) */
.pagination-link {
    background-color: transparent;
    border: 1px solid rgb(50, 80, 179);
    color: rgb(50, 80, 179);
}

/* Boutons pagination (hover) */
.pagination-link:hover {
    background-color: rgb(50, 80, 179);
    color: white;
}

/* Page courante */
.pagination .current {
    background-color: rgb(50, 80, 179);
    color: white;
    border: 1px solid rgb(50, 80, 179);
}

/* Media Queries pour le responsive */
@media (max-width: 768px) {
    .education-grid {
        grid-template-columns: 1fr; /* S'adapte à une seule colonne sur les petits écrans */
    }

    .education-container {
        padding: 15px;
    }

    .education-card {
        padding: 1.5rem;
    }
}

'''


############### Nouveau style

'''

/* Styles pour le corps de la page */
body {
    font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f7f9;
    color: #333;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* Styles pour les boutons de navigation */
.navigation-buttons {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    padding: 0 20px;
    box-sizing: border-box;
    margin-top: 20px;
    margin-bottom: 40px;
    position: absolute;
    top: 80px;
    left: 0;
    right: 0;
}

.nav-button {
    display: flex;
    align-items: center;
    gap: 5px;
    padding: 12px 24px;
    background-color: transparent;
    color: rgb(50, 80, 179);
    text-decoration: none;
    font-weight: bold;
    border: 2px solid rgb(50, 80, 179);
    border-radius: 5px;
    transition: background-color 0.3s ease, color 0.3s ease;
}

.nav-button:hover {
    background-color: rgb(50, 80, 179);
    color: white;
}

/* Style pour les flèches */
.button-arrow {
    font-size: 1.2rem;
    line-height: 1;
}

/* Conteneur principal */
.education-container {
    max-width: 1000px;
    margin: 50px auto;
    padding: 20px;
    background-color: transparent;
}

/* Titre principal */
.education-container h2 {
    text-align: center;
    margin-bottom: 30px;
    color: #333;
    margin-top: 100px;
}

/* Grille des expériences */
.education-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr); /* CORRIGÉ: Force 2 colonnes sur les grands écrans */
    gap: 20px;
}

/* Carte expérience */
.education-card {
    background: #ffffff;
    padding: 3rem;
    border-radius: 12px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    border-left: 5px solid rgb(50, 80, 179);
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    display: flex;
    flex-direction: column;
}

/* Effet de survol sur la carte */
.education-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
}

/* Alignement numéro + titre */
.education-header {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 15px;
}

/* Numéro circulaire */
.education-number {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background-color: rgb(50, 80, 179);
    color: white;
    font-size: 1.2rem;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

/* Titre expérience */
.education-degree {
    color: rgb(50, 80, 179);
    font-weight: bold;
    font-size: 1.2rem;
    margin: 0;
}

/* Ligne d'information (Organisation et Date) */
.info-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
    padding: 5px 0;
}

/* Label d'information */
.info-label {
    font-weight: 700;
    color: #bbb;
    font-size: 1rem;
}

/* Valeur d'information */
.info-value {
    font-weight: 600;
    color: #333;
    font-size: 1rem;
}

/* Valeur de date */
.date-value {
    color: #333;
    font-weight: bold;
}

/* Description */
.education-description {
    font-size: 1rem;
    color: #555;
    line-height: 1.6;
    margin: 15px 0;
    padding-top: 10px;
    border-top: 1px solid #eee;
    flex-grow: 1;
}

/* Lien de certification */
.certification-link {
    display: inline-block;
    padding: 10px 20px;
    background-color: transparent;
    color: rgb(50, 80, 179);
    text-decoration: none;
    font-weight: bold;
    border: 2px solid rgb(50, 80, 179);
    border-radius: 5px;
    transition: background-color 0.3s ease, color 0.3s ease;
    margin-top: 15px;
    align-self: flex-start;
}

.certification-link:hover {
    background-color: rgb(50, 80, 179);
    color: white;
}

/* Pagination */
/* Pagination */
.pagination {
    margin-top: 40px;
    margin-bottom: 50px;
    text-align: center;
    width: 100%;
}

.pagination .step-links {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap; /* évite le débordement */
    gap: 10px;
}

.pagination-link,
.pagination .current {
    display: inline-block;
    padding: 8px 16px;
    margin: 0;
    border-radius: 5px;
    font-weight: bold;
    text-decoration: none;
    transition: background-color 0.3s, color 0.3s;
    white-space: nowrap; /* empêche les retours à la ligne dans le texte */
}

/* Boutons pagination (normal) */
.pagination-link {
    background-color: transparent;
    border: 1px solid rgb(50, 80, 179);
    color: rgb(50, 80, 179);
}

/* Boutons pagination (hover) */
.pagination-link:hover {
    background-color: rgb(50, 80, 179);
    color: white;
}

/* Page courante */
.pagination .current {
    background-color: rgb(50, 80, 179);
    color: white;
    border: 1px solid rgb(50, 80, 179);
}

/* Media Queries pour le responsive */
@media (max-width: 768px) {
    .education-grid {
        grid-template-columns: 1fr; /* S'adapte à une seule colonne sur les petits écrans */
    }

    .education-container {
        padding: 15px;
    }

    .education-card {
        padding: 1.5rem;
    }
}


/* Overlay PDF */
.overlay {
    display: none;
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: rgba(0,0,0,0.7);
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.certificate-container {
    position: relative;
    width: 90%;
    height: 90%;
    max-width: 1000px;
    background: #fff;
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    overflow: hidden;
}

.close-btn {
    position: absolute;
    top: 10px; right: 20px;
    font-size: 2rem;
    cursor: pointer;
    color: red;
    font-weight: bold;
    z-index: 1001;
}

/* Toolbar PDF */
.certificate-toolbar {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
    padding: 10px;
    background: #f1f1f1;
    border-bottom: 1px solid #ddd;
}

.certificate-toolbar button {
    padding: 5px 10px;
    border: 1px solid rgb(50, 80, 179);
    background: white;
    color: rgb(50, 80, 179);
    border-radius: 5px;
    cursor: pointer;
    font-weight: bold;
}

.certificate-toolbar button:hover {
    background: rgb(50, 80, 179);
    color: white;
}

/* Contenu PDF */
.certificate-content {
    flex: 1;
    overflow: auto;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding: 10px;
}

.certificate-content canvas {
    max-width: 100%;
    height: auto;
}

/* Responsive */
@media (max-width: 768px) {
    .education-grid {
        grid-template-columns: 1fr;
    }
}

'''




'''

{% extends 'base.html' %}
{% load static %}

{% block extra_css %}
    <link rel="stylesheet" href="{% static 'skill/css/skill.css' %}">
{% endblock %}

{% block content %}

    <div class="navigation-buttons">
        <a href="{% url 'project' %}" class="nav-button">
            <span class="button-arrow">←</span> Projets
        </a>
        <a href="{% url 'contact' %}" class="nav-button">
            Contact <span class="button-arrow">→</span>
        </a>
    </div>

    <div class="education-container">
        <h2>Mes Expériences et Certifications</h2>

        <div class="education-grid">
            {% for experience in page_obj %}
            <div class="education-card">
                <div class="education-header">
                    <div class="education-number">{{ page_obj.start_index|add:forloop.counter0 }}</div>
                    <h3 class="education-degree">{{ experience.title }}</h3>
                </div>
                <div class="info-row">
                    <span class="info-label">Organisation</span>
                    <span class="info-value">{{ experience.organization }}</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Date</span>
                    <span class="info-value date-value">{{ experience.date }}</span>
                </div>
                <p class="education-description">{{ experience.description | safe}}</p>
                {% if experience.certification_file %}
                <a href="{{ experience.certification_file.url }}" target="_blank" class="certification-link">Voir la certification</a>
                <!--  -->
                {% endif %}
<!--  -->


            </div>
            {% endfor %}
        </div>
    </div>

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
{% endblock %}

'''