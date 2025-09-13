from django.contrib import admin

# admin.py
from django.contrib import admin
from .models import AboutMe
from ckeditor.widgets import CKEditorWidget
from django import forms

# Formulaire custom pour utiliser CKEditor
class AboutMeAdminForm(forms.ModelForm):
    presentation = forms.CharField(widget=CKEditorWidget(), required=False)
    professional_evolution = forms.CharField(widget=CKEditorWidget(), required=False)
    vision = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = AboutMe
        fields = '__all__'

# Admin
@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    form = AboutMeAdminForm
    list_display = ('id', 'photo', 'presentation', 'professional_evolution', 'vision')
    search_fields = ('presentation', 'professional_evolution', 'vision')


# # Enregistrer le modèle About dans l'admin
# @admin.register(About)
# class AboutAdmin(admin.ModelAdmin):
#     list_display = ('id', 'profile_image', 'description', 'goals')  # Champs à afficher dans la liste
#     search_fields = ('description', 'goals')       # Champs pour la recherche

'''
Étudiant en Licence 3 en Génie Logiciel option Analyse de Données, je suis passionné par l'IA et l'exploitation des données pour résoudre des problèmes complexes.
'''


'''
Mon objectif est de contribuer à des projets innovants en tant que Data Analyst ou Data Scientist, en appliquant mes compétences en analyse de données, machine learning et visualisation pour optimiser les processus décisionnels et créer de la valeur ajoutée. Je souhaite intégrer une équipe dynamique pour continuer à apprendre et participer à des projets à fort impact.
'''