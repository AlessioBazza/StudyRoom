from django.db import models
from datetime import datetime
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
        """
        Ritorna la lista di segnalazioni riguardanti quest'aula
        piu' recenti di adesso - intervallo
        """
        recenti = Posti.get_posti_recenti(interval)
        return recenti.filter(aula=self)

    def ultimo_aggiornamento(self):
        """
        Ritorna il timestamp dell'ultima segnalazione su quest'aula
        """
        segnalazioni = self.posti_set.order_by('-timestamp')
        return segnalazioni[0].timestamp if segnalazioni else None

    def stat(self, interval=settings.POSTI_DISPLAY_INTERVAL):
        """
        Ritorna la media dei posti liberi calcolate sulle segnalazioni piu'
        recenti di adesso - intervallo
        """
        # TODO inserire anche la deviazione standard?
        stat = self.get_posti_recenti(interval).aggregate(media=models.Avg('posti_liberi'),
                                                          numero=models.Count('id'))
        stat['interval'] = interval
        return stat

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
