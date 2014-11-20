from django.db import models
from datetime import datetime, timedelta
from sito import settings


class Stabili(models.Model):
    nome = models.CharField(max_length=30)

    def __unicode__(self):
        return self.nome


class Aule(models.Model):
    nome = models.CharField(max_length=20)
    piano = models.IntegerField()
    dimensione = models.IntegerField()
    locazione = models.ForeignKey(Stabili)

    def get_posti_recenti(self, interval=settings.POSTI_DISPLAY_INTERVAL):
        recenti = Posti.get_posti_recenti(interval)
        return recenti.filter(aula=self)

    def __unicode__(self):
        return self.nome


class Posti(models.Model):
    class Meta:
        ordering = ['-timestamp']

    timestamp = models.DateTimeField(auto_now=True)
    posti_liberi = models.IntegerField()
    user = models.CharField(max_length=50)
    aula = models.ForeignKey(Aule)
    chaos = models.BooleanField(default=False)
    lesson = models.BooleanField(default=False)

    @classmethod
    def get_posti_recenti(cls, interval=settings.POSTI_DISPLAY_INTERVAL):
        timestamp_from = settings.TIMEZONE.localize(datetime.now()) - interval
        return cls.objects.filter(timestamp__gte=timestamp_from)

    def save(self, *args, **kwargs):
        # TODO abort saving if user has recently voted for the same room
        self.timestamp = settings.TIMEZONE.localize(datetime.now())
        super(Posti, self).save(*args, **kwargs)
