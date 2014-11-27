from django.db import models
from datetime import datetime
from sito import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        validators = []
        if isinstance(max_value, int):
            validators.append(MaxValueValidator(max_value))
        if isinstance(min_value, int):
            validators.append(MinValueValidator(min_value))

        models.IntegerField.__init__(
            self,
            verbose_name,
            name,
            validators=validators,
            **kwargs
        )

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


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
        Ritorna delle statistiche calcolate sulla base dei report piu'
        recenti di adesso - intervallo o None se non ci sono report
        """
        # TODO inserire anche la deviazione standard?
        recenti = self.get_posti_recenti(interval)
        numero = recenti.count()

        if numero > 0:
            stat = {
                'numero': recenti.count(),
                'ghetto': 100 * recenti.filter(chaos=True).count() / float(numero),
                'lesson': 100 * recenti.filter(lesson=True).count() / float(numero),
                'interval': interval,
            }
            stat.update(recenti.aggregate(posti_liberi=models.Avg('posti_liberi')))
        else:
            stat = None

        return stat

    def __unicode__(self):
        return self.nome


class Posti(models.Model):
    class Meta:
        ordering = ['-timestamp']

    timestamp = models.DateTimeField(auto_now=True)
    posti_liberi = IntegerRangeField(min_value=0, max_value=100)
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
