from api import models
from django.core.management.base import BaseCommand, CommandError
import json
import os
import random


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_dati = os.path.join(os.path.dirname(__file__), 'dati.json')
        with open(file_dati) as f:
            dati = json.loads(f.read())

        lista_aule = list()
        for stabile, aule in dati.iteritems():
            s = models.Stabili(nome=stabile)
            s.save()

            for aula in aule:
                print 'creazione di', aula['nome']
                aula['locazione'] = s
                a = models.Aule(**aula)
                a.save()
                lista_aule.append(a)

        models.Posti(posti_liberi=90, user='aa', aula=random.choice(lista_aule),
                     chaos=True, lesson=False).save()
        models.Posti(posti_liberi=5, user='bb', aula=random.choice(lista_aule),
                     chaos=False, lesson=True).save()
        models.Posti(posti_liberi=70, user='cc', aula=random.choice(lista_aule),
                     chaos=True, lesson=False).save()
        models.Posti(posti_liberi=25, user='dd', aula=random.choice(lista_aule),
                     chaos=False, lesson=False).save()