import models
from rest_framework import serializers, viewsets, generics, mixins, permissions
from ipware.ip import get_real_ip
from django.http import Http404


class SerializerStabili(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Stabili
        fields = ('nome',)


class SerializerListaPosti(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(read_only=True)
    posti_liberi = serializers.IntegerField(read_only=True)

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


class SerializerAule(serializers.ModelSerializer):
    posti_set = SerializerListaPosti(many=True)

    class Meta:
        model = models.Aule
        fields = ('nome', 'piano', 'dimensione', 'id',  'posti_set')


class AuleView(viewsets.ModelViewSet):
    serializer_class = SerializerAule
    queryset = models.Aule.objects.all()

    permission_classes = [
        permissions.AllowAny
    ]


class PostiView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):

    permission_classes = [
        permissions.AllowAny
    ]

    queryset = models.Posti.objects.all()

    def get_serializer_class(self):
        assert self.action in ['list', 'create']
        return SerializerListaPosti if self.action == 'list' else SerializerAggiungiPosti

    def pre_save(self, obj):
        ip = '127.0.0.1'    # FIXME
        user = models.Utenti.objects.get(ip_address=ip)
        if not user:
            user = models.Utenti(ip_address=ip)
            user.save()

        obj.user = user

    def get_queryset(self):
        # TODO ritornare solo quelli piu' recenti di 30 minuti da ora
        return models.Posti.objects.all()