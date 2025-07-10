from operator import truediv

from django.shortcuts import render, redirect
from bibliothecaire.models import Borrower, Book, Dvd, Cd, BoardGame, Media, Borrow
from bibliothecaire.forms import CreateBorrower, CreateBook,CreateBorrow, CreateBg, UpdateBook,UpdateCd, UpdateBg,  CreateDvd, CreateCd, UpdateDvd
# Create your views here.

def borrowers_list(request):
    borrowers =  Borrower.objects.all()
    return render(request, 'borrowerList.html', {'borrowers' : borrowers })


def media_list(request):
    dvds = Dvd.objects.all()
    books = Book.objects.all()
    cds = Cd.objects.all()
    bgs = BoardGame.objects.all()
    return render(request, 'mediaList.html', {'dvds' : dvds , 'books' : books, 'cds' : cds, 'bgs' : bgs})


def borrow_list(request):
    borrows = Borrow.objects.all()
    return render(request, 'borrowList.html', {'borrows' : borrows})


def add_borrower(request):
    if request.method == 'POST':
        create_borrower = CreateBorrower(request.POST)
        if create_borrower.is_valid():
            borrower = Borrower()
            borrower.name = create_borrower.cleaned_data['nom']
            borrower.save()

            return redirect("/borrowerslist/")
    else:
        create_borrower = CreateBorrower()
        return render(request,
                      'addBorrower.html',
                      {'create_borrower': create_borrower})



def add_book(request):
        if request.method == 'POST':
            create_book = CreateBook(request.POST)
            if create_book.is_valid():
                book = Book()
                book.name = create_book.cleaned_data['nom']
                book.author = create_book.cleaned_data['auteur']
                book.save()

            return redirect("/")
        else:
            create_book = CreateBook()
        return render(request,
                      'addBook.html',
                      {'create_book': create_book})


def add_dvd(request):
    if request.method == 'POST':
        create_dvd = CreateDvd(request.POST)
        if create_dvd.is_valid():
            dvd = Dvd()
            dvd.name = create_dvd.cleaned_data['nom']
            dvd.director = create_dvd.cleaned_data['realisateur']
            dvd.save()
        return redirect("/")
    else:
        create_dvd = CreateDvd()
    return render(request,
                  'addDvd.html',
                  {'create_dvd': create_dvd})


def add_cd(request):
    if request.method == 'POST':
        create_cd = CreateCd(request.POST)
        if create_cd.is_valid():
            cd = Cd()
            cd.name = create_cd.cleaned_data['nom']
            cd.artist = create_cd.cleaned_data['artiste']
            cd.save()
        return redirect("/")
    else:
        create_cd = CreateCd()
    return render(request,
                  'addCd.html',
                  {'create_cd': create_cd})


def add_bg(request):
    if request.method == 'POST':
        create_bg = CreateBg(request.POST)
        if create_bg.is_valid():
            bg = BoardGame()
            bg.name = create_bg.cleaned_data['nom']
            bg.creator = create_bg.cleaned_data['createur']
            bg.save()
        return redirect("/")
    else:
        create_bg = CreateBg()
    return render(request,
                  'addBg.html',
                  {'create_bg': create_bg})


def update_book(request, id):
        if request.method == 'POST':
            book = Book.objects.get(pk=id)
            updatebook = UpdateBook(request.POST)
            if update_book.is_valid():
                book.name = updatebook.cleaned_data['nom']
                book.auteur = updatebook.cleaned_data['auteur']
                book.save()
            return redirect("/")
        else:
            updatebook = UpdateBook()
            book = Book.objects.get(pk=id)
            return render(request,
                          'updateBook.html',
                          {'update_book': updatebook, 'book': book}
                          )


def update_dvd(request, id):
    if request.method == 'POST':
        dvd = Dvd.objects.get(pk=id)
        updatedvd = UpdateDvd(request.POST)
        if updatedvd.is_valid():
            dvd.name = update_dvd.cleaned_data['nom']
            dvd.director = update_dvd.cleaned_data['realisateur']
            dvd.save()
        return redirect("/")
    else:
        updatedvd =UpdateDvd()
        dvd = Dvd.objects.get(pk=id)
        return render(request,
                      'updateDvd.html',
                      {'update_dvd': updatedvd, 'dvd': dvd}
                      )

def update_bg(request, id):
    if request.method == 'POST':
        bg = BoardGame.objects.get(pk=id)
        updatebg = UpdateBg(request.POST)
        if updatebg.is_valid():
            bg.name = update_bg.cleaned_data['nom']
            bg.creator = update_bg.cleaned_data['créateur']
            bg.save()
        return redirect("/")
    else:
        updatebg = UpdateBg()
        bg = BoardGame.objects.get(pk=id)
        return render(request,
                      'updateBg.html',
                      {'update_bg': updatebg, 'bg': bg}
                      )

def update_cd(request, id):
    if request.method == 'POST':
        cd = Cd.objects.get(pk=id)
        updatecd = UpdateCd(request.POST)
        if updatecd.is_valid():
            cd.name = update_bg.cleaned_data['nom']
            cd.creator = update_bg.cleaned_data['artiste']
            cd.save()
        return redirect("/")
    else:
        updatecd = UpdateCd()
        cd = Cd.objects.get(pk=id)
        return render(request,
                      'updateCd.html',
                      {'update_cd': updatecd, 'cd': cd}
                      )

def delete_media(request, id):
    media = Media.objects.get(pk=id)
    media.delete()
    medias = Book.objects.all()
    return render(request, 'mediaList.html',
                  {'medias': medias})


def delete_dvd(request, id):
    dvd = Dvd.objects.get(pk=id)
    dvd.delete()
    dvds = Dvd.objects.all()
    return render(request, 'mediaList.html',
                  {'dvds': dvds})


def delete_cd(request, id):
    cd = Cd.objects.get(pk=id)
    cd.delete()
    cds = Cd.objects.all()
    return render(request, 'mediaList.html',
                  {'cds': cds})


def delete_bg(request, id):
    bg = BoardGame.objects.get(pk=id)
    bg.delete()
    bgs = BoardGame.objects.all()
    return render(request, 'mediaList.html',
                  {'bgs': bgs})

def delete_borrower(request, id):
    borrower = Borrower.objects.get(pk=id)
    borrower.delete()
    borrowers  = Borrower.objects.all()
    return render(request, 'borrowerList.html',
                  {'borrowers': borrowers})

def delete_borrow(request, id):
    borrow = Borrow.objects.get(pk=id)
    media = borrow.media
    media.available = True
    media.save()
    borrow.delete()
    borrows = Borrow.objects.all()
    return render(request, 'borrowList.html', {'borrows': borrows})

def create_borrow(request, id):
    media = Media.objects.get(pk=id)
    if request.method == 'POST':
        form = CreateBorrow(request.POST)
        if form.is_valid():
            borrow = Borrow()
            borrow.media = media
            borrow.borrower = form.cleaned_data['emprunteur']
            media.available = False
            media.save()
            borrow.save()
        return redirect("/borrowlist/")
    else:
        form = CreateBorrow()
    return render(request, 'createBorrow.html',
                  {'form': form, 'media': media})