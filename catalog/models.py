# -*- coding: utf-8 -*-
from __future__ import unicode_literals


import uuid # Required for unique book instances

from django.db import models

# Create your models here.
from django.urls import reverse


class Genre(models.Model):
    """
    Model to represent a book model, eg Scientfic, Fictional
    """
    name = models.CharField(max_length=200,help_text="Enter a Book genre(e.g Science fiction, Poetry)")

    def __str__(self):
        """
        
        :return the book genre name in admine site: 
        """
        return self.name

# Language model
class Language(models.Model):

    name = models.CharField(max_length=200,help_text="Select a book's Language")

    def __str__(self):
        return self.name


# Book model class
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author',on_delete=models.SET_NULL,null=True)
    summary = models.TextField(max_length=200,help_text="Enter a brief description of the book")
    isbn    = models.CharField('ISBN',max_length=13,help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre  = models.ManyToManyField(Genre,help_text="Select a Genre for this book")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        return the absolute url of a given book instance
        :return: 
        """
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """
                Creates a string for the Genre. This is required to display genre in Admin.
         """
        return ','.join([genre.name for genre in self.genre.all()[:3]])
    display_genre.short_description = 'Genre'



class BookInstance(models.Model):
    """
    model representation of a specfic book that can be borrowed
    """
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Unique ID for this book in the library")
    book = models.ForeignKey('Book',on_delete=models.SET_NULL,null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True,blank=True)

    LOAN_STATUS = (
        ('m' , 'Maintenance'),
        ('o' , 'On Loan'),
        ('a' , 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length =1,choices = LOAN_STATUS,blank =True,default = 'm',help_text = "Book availability")

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return '%s (%s)' %(self.id,self.book.title)

class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname  = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True,blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
              Returns the url to access a particular author instance.
         """
        return reverse('author-detail',args=[str(self.id)])

    def __str__(self):
        return '%s, %s ' %(self.firstname,self.lastname)
