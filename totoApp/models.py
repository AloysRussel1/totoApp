from django.db import models

from django.db import models

class Toto(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    photo = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f"{self.nom} {self.prenom}"

