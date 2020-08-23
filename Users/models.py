# -*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.TextField('Email', blank=True)
    number = models.IntegerField('Number')
    created = models.DateTimeField('Created', auto_now_add=True)
    changed = models.DateTimeField('Changed', auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('user_edit', kwargs={'pk': self.pk})
