# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Author,Book,BookInstance,Language,Genre
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'date_of_birth', 'date_of_death')
    fields = ['firstname','lastname',('date_of_birth', 'date_of_death')]

admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)
#admin.site.register(BookInstance)
#admin.site.register(Book)
admin.site.register(Language)

# Register the Admin classes for Book using the decorator


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None,{
            'fields' : ('book','imprint','id')
        }),
        ('Availability', {
            'fields' : ('status','due_back')
        }),
    )

