from rest_framework import serializers, mixins, permissions
from extensions import MultiSerializer
import models


class SerializerListaPosti(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField()
    posti_liberi = serializers.IntegerField()

    aula = serializers.Field(source='aula.nome')

    class Meta:
        model = models.Posti
        exclude = ('id', 'user')


class SerializerAggiungiPosti(serializers.ModelSerializer):
    aula = serializers.PrimaryKeyRelatedField()
    posti_liberi = serializers.IntegerField()

    class Meta:
        model = models.Posti
        exclude = ('id', 'user', 'timestamp')


class PostiView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                MultiSerializer):

    queryset = models.Posti.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_mapping = {
        'list': SerializerListaPosti,
        'create': SerializerAggiungiPosti,

    }

    def pre_save(self, obj):
        ip = '127.0.0.1'    # FIXME
        try:
            user = models.Utenti.objects.get(ip_address=ip)
        except models.Utenti.DoesNotExist:
            user = models.Utenti(ip_address=ip)
            user.save()

        obj.user = user

    def get_queryset(self):
        # TODO ritornare solo quelli piu' recenti di 30 minuti da ora
        return models.Posti.objects.all()