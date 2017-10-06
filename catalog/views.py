# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Book,BookInstance,Author,Genre
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    """
    view function for home page
    :return: 
    """
    num_books     = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #number of visits to this view ,as counted in the session variables
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # available books with (status = 'a)
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    return render(request,'index.html',context={'num_books' : num_books,'num_instances' : num_instances,'num_instances_available' : num_instances_available,'num_authors' :num_authors,'num_visits':num_visits},)

class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book

class LoanBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """
        Generic class-based view listing books on loan to current user. 
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

