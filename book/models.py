# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=120)
    cover = models.URLField(max_length=120)
    isbn = models.CharField(max_length=120)
    uri = models.CharField(max_length=120)
    author = models.CharField(max_length=120)


    def __str__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})