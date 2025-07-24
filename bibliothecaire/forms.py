from django import forms
from bibliothecaire.models import Borrower

class CreateBorrower(forms.Form):
    nom = forms.CharField(required=True)

class CreateBook(forms.Form):
    nom = forms.CharField(required=True)
    auteur = forms.CharField(required=True)

class CreateDvd(forms.Form):
    nom = forms.CharField(required=True)
    realisateur = forms.CharField(required=True)

class CreateCd(forms.Form):
        nom = forms.CharField(required=True)
        artiste = forms.CharField(required=True)

class CreateBg(forms.Form):
    nom = forms.CharField(required=True)
    createur = forms.CharField(required=True)

class UpdateBook(forms.Form):
    nom = forms.CharField(required=True)
    auteur = forms.CharField(required=True)

class UpdateDvd(forms.Form):
    nom = forms.CharField(required=True)
    realisateur = forms.CharField(required=True)

class UpdateCd(forms.Form):
    nom = forms.CharField(required=True)
    artiste = forms.CharField(required=True)

class UpdateBg(forms.Form):
    nom = forms.CharField(required=True)
    createur = forms.CharField(required=True)

class CreateBorrow(forms.Form):
    emprunteur = forms.ModelChoiceField(queryset=Borrower.objects.filter(borrows__lte=2), required=True)
