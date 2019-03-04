from django import forms
from .models import Commentaire

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 12}))
    envoyeur = forms.EmailField(label="votre adresse mail")
    renvoi = forms.BooleanField(help_text="cochez pour recevoir une copie du mail envoyé", required=False)

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        exclude = ('article',)