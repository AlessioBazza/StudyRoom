from rest_framework import serializers, mixins, viewsets, generics, permissions
import extensions, models, aule


class SerializerListaStabili(serializers.ModelSerializer):
    class Meta:
        model = models.Stabili
        fields = ('id', 'nome',)


class SerializerDettaglioStabili(serializers.ModelSerializer):
    aule_set = aule.SerializerListaAule(many=True)

    class Meta:
        model = models.Stabili
        fields = ('id', 'nome', 'aule_set',)


class StabiliView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  extensions.MultiSerializer,
                  extensions.MultiPermissions):

    queryset = models.Stabili.objects.all()

    default_serializer = SerializerListaStabili
    serializer_mapping = {
        'list': SerializerListaStabili,
        'create': SerializerDettaglioStabili,
        'retrieve': SerializerDettaglioStabili,
        'update': SerializerDettaglioStabili,
    }

    default_permissions = permissions.IsAdminUser
    permission_mapping = {
        'list': permissions.AllowAny,
        'retrieve': permissions.AllowAny,
        'create': permissions.IsAdminUser,
        'update': permissions.IsAdminUser,
    }