from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, default='Default Name')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
