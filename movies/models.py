from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse


class timemixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Categories (timemixin):
    category = models.CharField(max_length=35, unique=True)

    def __str__(self):
        return "{}".format(self.category)

    def get_absolute_url(self):
       return reverse('movies:index')

class Villans(timemixin):
    CHOICE = [('BAD','BAD'), ('GOOD','GOOD')]
    name = models.CharField(max_length=35, unique=True)
    character=models.CharField(max_length=15, choices=CHOICE)
    category = models.ForeignKey(Categories)


    def get_absolute_url(self):
        return reverse('movies:index')

    def __str__(self):
        return "{}".format(self.character, self.name)