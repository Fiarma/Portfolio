from django.contrib import admin
from .models import Project, EtapeResolution, ResultatModele, Metrique, LeconApprise, AmeliorationPossible

# Inlines pour les modèles qui sont directement liés à un projet
class EtapeResolutionInline(admin.TabularInline):
    model = EtapeResolution
    extra = 1

class ResultatModeleInline(admin.TabularInline):
    model = ResultatModele
    extra = 1

class LeconAppriseInline(admin.TabularInline):
    model = LeconApprise
    extra = 1

class AmeliorationPossibleInline(admin.TabularInline):
    model = AmeliorationPossible
    extra = 1

# Classe d'administration pour le modèle Metrique
class MetriqueAdmin(admin.ModelAdmin):
    list_display = ('nom', 'valeur', 'resultat')  # Affiche ces colonnes
    list_filter = ('resultat__nom_modele',)  # Permet de filtrer par nom de modèle
    search_fields = ('nom', 'valeur')

# Classe d'administration pour le modèle ResultatModele
class ResultatModeleAdmin(admin.ModelAdmin):
    list_display = ('nom_modele', 'project')
    list_filter = ('project',)
    search_fields = ('nom_modele',)


# Enregistrement des modèles
admin.site.register(Project)  # On enregistre le projet pour pouvoir le gérer seul
admin.site.register(EtapeResolution)
admin.site.register(ResultatModele, ResultatModeleAdmin)
admin.site.register(Metrique, MetriqueAdmin)
admin.site.register(LeconApprise)
admin.site.register(AmeliorationPossible)