# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView,ListView
from django.urls import reverse_lazy
from .models import Book

class BookCreate(CreateView):
    model = Book
    fields = ['title']

class BookUpdate(UpdateView):
    model = Book
    fields = ['title']
    template_name_suffix = '_update_form'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')

class BookDetailView(DetailView):
    model = Book

class BookListView(ListView):
    model = Book