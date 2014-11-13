from api.models import Stabili, Aule, Utenti, Posti
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):  
      def handle(self, *args, **options):
            s = Stabili(nome='Polo Ferrari')
            s.save()
            a1 = Aule(nome='A101',piano=-1,dimensione=180,locazione=s)
            a1.save()
            a2 = Aule(nome='A102',piano=-1,dimensione=150,locazione=s)
            a2.save()
            a3 = Aule(nome='A103',piano=-1,dimensione=150,locazione=s)
            a3.save()
            a4 = Aule(nome='A104',piano=-1,dimensione=150,locazione=s)
            a4.save()
            a5 = Aule(nome='A105',piano=-1,dimensione=150,locazione=s)
            a5.save()
            a6 = Aule(nome='A106',piano=-1,dimensione=150,locazione=s)
            a6.save()
            a7 = Aule(nome='AulaStudio',piano=-1,dimensione=50,locazione=s)
            a7.save()
            a8 = Aule(nome='A203',piano=0,dimensione=70,locazione=s)
            a8.save()
            a9 = Aule(nome='A202',piano=0,dimensione=70,locazione=s)
            a9.save()
            a0 = Aule(nome='A201',piano=0,dimensione=70,locazione=s)
            a0.save()

            u1 = Utenti(code='aaa')
            u1.save()
            u2 = Utenti(code='bbb')
            u2.save()
            u3 = Utenti(code='ccc')
            u3.save()

            p1 = Posti(posti_liberi=90,user = u2,aula=a4,chaos = True,lesson=False)
            p1.save()
            p2 = Posti(posti_liberi=5,user = u3,aula=a8,chaos = False,lesson=True)
            p2.save()
            p3 = Posti(posti_liberi=70,user = u1,aula=a2,chaos = True,lesson=False)
            p3.save()
            p4 = Posti(posti_liberi=25,user = u2,aula=a3,chaos = False,lesson=False)
            p4.save()
            
        
