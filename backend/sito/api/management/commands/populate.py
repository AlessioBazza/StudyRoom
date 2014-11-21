from api import models
from django.core.management.base import BaseCommand
import json
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_dati = os.path.join(os.path.dirname(__file__), 'dati.json')
        with open(file_dati) as f:
            dati = json.loads(f.read())

        for stabile, aule in dati.iteritems():
            s = models.Stabili(nome=stabile)
            s.save()

            for aula in aule:
                print 'creazione di', aula['nome']
                models.Aule(locazione=s, **aula).save()