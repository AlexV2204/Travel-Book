from django.db import models


class Voyage(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    categorie = models.CharField(max_length=100)
    contenu = models.CharField(max_length=10000)
    image = models.ImageField()

    def __str__(self):
        return self.destination
