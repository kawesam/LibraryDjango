# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Book,BookInstance,Author,Genre
from django.views import generic

# Create your views here.

def index(request):
    """
    view function for home page
    :return: 
    """
    num_books     = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # available books with (status = 'a)
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    return render(request,'index.html',context={'num_books' : num_books,'num_instances' : num_instances,'num_instances_available' : num_instances_available,'num_authors' :num_authors},)

class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book


