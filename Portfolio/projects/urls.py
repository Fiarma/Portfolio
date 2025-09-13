from django.urls import path
from . import views

urlpatterns = [
    path('', views.project, name='project'),

    # URL pour afficher les détails d'un projet spécifique
    path('<int:project_id>/', views.project_detail_view, name='project-detail'),
]