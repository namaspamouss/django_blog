from django.contrib import admin
from .models import Article, Auteur, Commentaire
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre','date','auteur')
    list_filter = ('date','auteur')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'description')

class CommentaireAdmin(admin.ModelAdmin):
    list_display = ('pseudo', 'email', 'contenu', 'article')
    list_filter = ('pseudo', 'article')
    ordering = ('article',)
    search_fields = ('pseudo','contenu')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Auteur)
admin.site.register(Commentaire, CommentaireAdmin)