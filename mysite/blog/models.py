from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    visible = models.BooleanField(default=False)
    auteur = models.ForeignKey('Auteur',on_delete=models.CASCADE)

    class Meta:
        verbose_name = "article"
        ordering = ['-date']

    def __str__(self):
        return self.titre


class Auteur(models.Model):
    nom = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='avatar/')

    class Meta:
        verbose_name = "auteur"

    def __str__(self):
        return self.nom


class Commentaire(models.Model):
    pseudo = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    contenu = models.TextField()
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "commentaire"

    def __str__(self):
        return "commentaire de {}".format(self.pseudo)