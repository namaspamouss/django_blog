from django.shortcuts import render, get_object_or_404
from blog.models import Article, Auteur, Commentaire
from .forms import ContactForm, CommentaireForm


def home(request):
    articles = Article.objects.all()
    texte = "coucou"
    return render(request,'blog/home.html', locals())

def article(request, id):
    article = get_object_or_404(Article, id=id)
    commentaires = Commentaire.objects.filter(article_id=id)
    form = CommentaireForm(request.POST)
    if form.is_valid():
        commentaire = form.save(commit=False)
        commentaire.article_id=id
        form.save()
        envoi = True
    else:
        form = CommentaireForm()
    return render(request,'blog/article.html', locals())

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        sujet = form.cleaned_data["sujet"]
        message = form.cleaned_data["message"]
        envoyeur = form.cleaned_data["envoyeur"]
        renvoi = form.cleaned_data["renvoi"]
        envoi = True
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', locals())