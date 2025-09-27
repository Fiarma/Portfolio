# # projects/models.py
# from django.db import models
# from ckeditor.fields import RichTextField

# class Project(models.Model):
#     titre = models.CharField(max_length=200)
#     date_creation = models.DateField()
#     description_probleme = RichTextField(blank=True, null=True)
#     justification = RichTextField(blank=True, null=True)
#     objective = RichTextField(blank=True, null=True)
#     donnees_utilisees = RichTextField(blank=True, null=True)
#     tools = RichTextField(blank=True, null=True)
#     lien_code = models.URLField(max_length=200, blank=True, null=True, help_text="Lien vers le dépôt GitHub ou Google Colab du projet.")

#     def __str__(self):
#         return self.titre

#     class Meta:
#         ordering = ['-date_creation']
#         verbose_name_plural = "projects"

# class EtapeResolution(models.Model):
#     project = models.ForeignKey(Project, related_name='etapes', on_delete=models.CASCADE)
#     nom = models.CharField(max_length=100)
#     description = RichTextField(blank=True, null=True)
#     def __str__(self):
#         return f"{self.nom} ({self.project.titre})"

# class ResultatModele(models.Model):
#     project = models.ForeignKey(Project, related_name='resultats_modeles', on_delete=models.CASCADE)
#     nom_modele = models.CharField(max_length=100)
#     resultats = RichTextField(blank=True, null=True)

#     def __str__(self):
#         return f"Résultats pour {self.nom_modele} ({self.project.titre})"

# class Metrique(models.Model):
#     resultat = models.ForeignKey(ResultatModele, related_name='metriques', on_delete=models.CASCADE)
#     nom = models.CharField(max_length=100)
#     valeur = models.CharField(max_length=50)

#     def __str__(self):
#         return f"{self.nom}: {self.valeur}"

# class Conclusion(models.Model):
#     project = models.ForeignKey(Project, related_name='conclusions', on_delete=models.CASCADE)
#     description = RichTextField(blank=True, null=True)

#     def __str__(self):
#         return f"Conclusion pour {self.project.titre}"

# class LeconApprise(models.Model):
#     project = models.ForeignKey(Project, related_name='lecons', on_delete=models.CASCADE)
#     titre = models.CharField(max_length=200)
#     description = RichTextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.titre} ({self.project.titre})"

# class AmeliorationPossible(models.Model):
#     project = models.ForeignKey(Project, related_name='ameliorations', on_delete=models.CASCADE)
#     titre = models.CharField(max_length=200)
#     description = RichTextField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.titre} ({self.project.titre})"


# projects/models.py
from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    titre = models.CharField(max_length=200)
    date_creation = models.DateField()
    description_probleme = RichTextField(blank=True, null=True)
    justification = RichTextField(blank=True, null=True)
    objective = RichTextField(blank=True, null=True)
    donnees_utilisees = RichTextField(blank=True, null=True)
    tools = RichTextField(blank=True, null=True)
    lien_code = models.URLField(max_length=200, blank=True, null=True, help_text="Lien vers le dépôt GitHub ou Google Colab du projet.")
    capture = models.ImageField(upload_to='project_captures/', blank=True, null=True, help_text="Capture d'écran ou image principale du projet.")

    def __str__(self):
        return self.titre

    class Meta:
        ordering = ['-date_creation']
        verbose_name_plural = "projects"

class EtapeResolution(models.Model):
    project = models.ForeignKey(Project, related_name='etapes', on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nom} ({self.project.titre})"

class ResultatModele(models.Model):
    project = models.ForeignKey(Project, related_name='resultats_modeles', on_delete=models.CASCADE)
    nom_modele = models.CharField(max_length=100)
    resultats = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"Résultats pour {self.nom_modele} ({self.project.titre})"

class Metrique(models.Model):
    resultat = models.ForeignKey(ResultatModele, related_name='metriques', on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    valeur = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom}: {self.valeur}"

class Conclusion(models.Model):
    project = models.ForeignKey(Project, related_name='conclusions', on_delete=models.CASCADE)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"Conclusion pour {self.project.titre}"

class LeconApprise(models.Model):
    project = models.ForeignKey(Project, related_name='lecons', on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titre} ({self.project.titre})"

class AmeliorationPossible(models.Model):
    project = models.ForeignKey(Project, related_name='ameliorations', on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    description = RichTextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titre} ({self.project.titre})"