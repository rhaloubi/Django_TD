from django.db import models
from etudiants.models import Etudiant

class Cours(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    code_cours = models.CharField(max_length=20, unique=True)
    etudiants = models.ManyToManyField(Etudiant, through='Inscription')

    def __str__(self):
        return self.titre

class Inscription(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    date_inscription = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['etudiant', 'cours']
