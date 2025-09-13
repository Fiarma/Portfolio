from django.db import models
from cloudinary.models import CloudinaryField  # Importer CloudinaryField

# Create your models here.
#from django.db import models

class About(models.Model):
    # Champ pour une image de profil
    #profile_image = models.ImageField(upload_to='about/')
    profile_image = CloudinaryField('image', folder='about/')  # Utiliser CloudinaryField


    # Champ pour une description
    description = models.TextField()

    # Champ pour les objectifs
    goals = models.TextField()

    def __str__(self):
        return "À Propos de Moi"
    
from django.db import models
from ckeditor.fields import RichTextField  # Pour le RichText

from django.db import models
from ckeditor.fields import RichTextField

class AboutMe(models.Model):
    photo = models.ImageField(upload_to='about/photos/', blank=True, null=True)
    presentation = RichTextField(blank=True, null=True)
    professional_evolution = RichTextField(blank=True, null=True)
    vision = RichTextField(blank=True, null=True)

    def __str__(self):
        return "À propos de moi"

