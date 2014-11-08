from rest_framework import serializers, mixins, permissions
from posti import SerializerListaPosti
import models, extensions


class SerializerListaAule(serializers.ModelSerializer):
    class Meta:
        model = models.Aule
        fields = ('nome', 'piano', 'dimensione', 'id', )


class SerializerDettaglioAule(serializers.ModelSerializer):
    posti_set = SerializerListaPosti(many=True, read_only=True)

    class Meta:
        model = models.Aule
        fields = ('nome', 'piano', 'dimensione', 'id', 'posti_set')


class SerializerAggiungiModificaAule(serializers.ModelSerializer):
    class Meta:
        model = models.Aule
        fields = ('nome', 'piano', 'dimensione', 'locazione')


class AuleView(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.UpdateModelMixin,
               mixins.RetrieveModelMixin,
               extensions.MultiSerializer,
               extensions.MultiPermissions):

    queryset = models.Aule.objects.all()

    default_serializer = SerializerListaAule
    serializer_mapping = {
        'list': SerializerListaAule,
        'retrieve': SerializerDettaglioAule,
        'update': SerializerAggiungiModificaAule,
        'create': SerializerAggiungiModificaAule,
    }

    default_permissions = permissions.IsAdminUser
    permission_mapping = {
        'list': permissions.AllowAny,
        'retrieve': permissions.AllowAny,
        'create': permissions.IsAdminUser,
        'update': permissions.IsAdminUser,
    }

