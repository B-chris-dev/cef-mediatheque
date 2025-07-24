from django.db import models
from django.forms import NullBooleanField


# Create your models here.
class Borrower(models.Model):
    name = models.fields.CharField(max_length=150)
    borrows = models.fields.DecimalField(max_digits=1, decimal_places=0, default='0')

    def __str__(self):
        return self.name

class Media(models.Model):
    name = models.fields.CharField(max_length=150)
    available = models.fields.BooleanField(default=True)

    def __str__(self):
        return self.name

class Book(Media):
    author = models.fields.CharField(max_length=150)



class Dvd(Media):
    director = models.fields.CharField(max_length=150)


class Cd(Media):
    artist = models.fields.CharField(max_length=150)


class BoardGame(models.Model):
    name = models.fields.CharField(max_length=150)
    creator = models.fields.CharField(max_length=150)


class Borrow(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    created_at = models.fields.DateTimeField(auto_now_add=True)

