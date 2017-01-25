from __future__ import unicode_literals
from allauth import app_settings
from django.db import models


class Email(models.Model):
    class Meta:
        verbose_name_plural = 'Emails'
        verbose_name = 'Emails'
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank = False, null = False, verbose_name = 'Creation Date')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank = False, null = False, verbose_name = 'Updated')
    email = models.CharField(max_length=3000, blank=True, null=True)

    def __unicode__(self):
        if not self.email:
            return "Fecha: %s" % self.created
        else:
            return "Email: %s" % self.email



class Route(models.Model):
    class Meta:
        verbose_name_plural = 'Ruta Colectiv'
        verbose_name = 'Ruta Colectiv'
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank = False, null = False, verbose_name = 'Creation Date')
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank = False, null = False, verbose_name = 'Updated')
    user = models.OneToOneField(app_settings.USER_MODEL, blank=True, null=True)
    destiny = models.CharField(max_length=3000, blank=True, null=True)
    origin = models.CharField(max_length=3000, blank=True, null=True)
    duration = models.CharField(max_length=3000, blank=True, null=True)
    distance = models.CharField(max_length=3000, blank=True, null=True)
    email = models.ForeignKey(Email, blank=True, null=True)

    def __unicode__(self):
        return "Fecha: %s" % self.created
