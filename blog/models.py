from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    publie = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.titre
    
    def est_recent(self):
        from django.utils import timezone
        from datetime import timedelta
        return self.date_creation >= timezone.now() - timedelta(days=7)
    
    def nb_de_mots(self):
        return len(self.contenu.split())
    
    def apercu(self, longueur=100):
        if len(self.contenu) > longueur:
            return f"{self.contenu[:longueur]} ..."
        return self.contenu
