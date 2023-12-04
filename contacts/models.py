from django.db import models

class Contact(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()
