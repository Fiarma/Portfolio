


# from django.db import models
# from cloudinary.models import CloudinaryField  # Importer CloudinaryField


# class Experience(models.Model):
#     title = models.CharField(max_length=200)  # Titre de la certification
#     organization = models.CharField(max_length=200)  # Organisation émettrice
#     year = models.CharField(max_length=50)  # Année d'obtention
#     description = models.TextField()  # Description de la certification
#     certification_file = models.FileField(upload_to='certifications/', blank=True, null=True)  # Fichier de certification
    
#     def __str__(self):
#         return f"{self.title} - {self.organization}"


from django.db import models
from ckeditor.fields import RichTextField

class Experience(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date = models.DateField(blank=True, null=True) # Changement du champ year en DateField
    description = RichTextField(blank=True, null=True)
    certification_file = models.FileField(upload_to='certifications/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} - {self.organization}"