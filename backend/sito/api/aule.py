from rest_framework import serializers, mixins, permissions, viewsets
from posti import SerializerPosti
import models


class SerializerAule(serializers.ModelSerializer):
    stat = serializers.Field(source='stat')
    ultimo_aggiornamento = serializers.Field(source='ultimo_aggiornamento')
    locazione = serializers.Field(source='locazione.nome')

    class Meta:
        model = models.Aule
        fields = ('id', 'nome', 'piano', 'dimensione', 'stat',
                  'ultimo_aggiornamento', 'locazione')


class SerializerRetrieveAule(serializers.ModelSerializer):
    stat = serializers.Field(source='stat')
    ultimo_aggiornamento = serializers.Field(source='ultimo_aggiornamento')
    posti_set = SerializerPosti(many=True)
    locazione = serializers.Field(source='locazione.nome')

    class Meta:
        model = models.Aule
        fields = ('nome', 'piano', 'dimensione', 'id', 'stat',
                  'ultimo_aggiornamento', 'posti_set', 'locazione')


class AuleView(mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet):

    queryset = models.Aule.objects.all()
    serializer_class = SerializerAule

    def get_serializer_class(self):
        return SerializerRetrieveAule if self.action == 'retrieve' else SerializerAule
