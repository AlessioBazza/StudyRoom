from django.db import models
import pytz
from datetime import datetime
from sito import settings


class Utenti(models.Model):
    code = models.CharField(max_length=20, primary_key=True, null=False)

    def __unicode__(self):
        return self.code

class Stabili(models.Model):
    nome = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nome

class Aule(models.Model):
    nome = models.CharField(max_length=20)
    piano = models.IntegerField()
    dimensione = models.IntegerField()
    locazione = models.ForeignKey(Stabili)

    def __unicode__(self):
        return self.nome


class Posti(models.Model):
    class Meta:
        ordering = ['-timestamp']

    timestamp = models.DateTimeField(auto_now=True)
    posti_liberi = models.IntegerField()
    user = models.ForeignKey(Utenti)
    aula = models.ForeignKey(Aule)
    chaos = models.BooleanField(default=False)
    lesson = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # TODO abort saving if user has recently voted for the same room
        self.timestamp = pytz.timezone(settings.TIME_ZONE).localize(datetime.now())
        super(Posti, self).save(*args, **kwargs)
