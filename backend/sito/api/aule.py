from rest_framework import serializers, mixins, permissions, viewsets
from posti import SerializerPosti
import models


class SerializerAule(serializers.ModelSerializer):
    posti_set = SerializerPosti(many=True, source='get_posti_recenti')

    class Meta:
        model = models.Aule
        fields = ('nome', 'piano', 'dimensione', 'id', 'posti_set')


class AuleView(mixins.ListModelMixin,
               mixins.RetrieveModelMixin,
               viewsets.GenericViewSet):

    queryset = models.Aule.objects.all()
    serializer_class = SerializerAule