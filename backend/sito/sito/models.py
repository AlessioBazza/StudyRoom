from django.db import models


class Utenti(models.Model):
        ip_address = models.IPAddressField()


class Aule(models.Model):
        nome = models.CharField(max_length=4)
        piano = models.IntegerField()
        dimensione = models.IntegerField()
        locazione = models.ForeignKey("Stabili")

class Stabili(models.Model):
        nome = models.CharField(max_length=30)

class Posti(models.Model):
        timestamp = models.DateTimeField()
        posti_liberi = models.IntegerField()
        user = models.ForeignKey("Utenti")
        aula = models.ForeignKey("Aule")


