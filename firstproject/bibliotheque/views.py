from django.shortcuts import render
from .forms import LivreForm
from . import models
# Create your views here.

def ajout(request):
    form = LivreForm()  # création d'un formulaire vide
    return render(request, "bibliotheque/ajout.html", {"form": form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"bibliotheque/affiche.html",{"livre" : livre})
    else:
        return render(request,"bibliotheque/ajout.html",{"form": lform})

def index(request):
    liste = models.Livre.objects.all()
    return render(request,"bibliotheque/index.html",{"liste":liste})

def affiche(request, id):
    livre = models.Livre.objects.get(pk=id)
    return render(request,"bibliotheque/affiche.html",{"livre":livre})