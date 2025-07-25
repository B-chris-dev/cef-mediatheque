from django.shortcuts import render
from bibliothecaire.models import Cd, Dvd, Book, BoardGame

def medias_list(request):
    dvds = Dvd.objects.all()
    books = Book.objects.all()
    cds = Cd.objects.all()
    bgs = BoardGame.objects.all()
    return render(request, 'mediasList.html', {'dvds' : dvds , 'books' : books, 'cds' : cds, 'bgs' : bgs})