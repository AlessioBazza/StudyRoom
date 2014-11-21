from rest_framework import serializers, mixins, viewsets, generics, permissions, viewsets
import models


class SerializerStabili(serializers.ModelSerializer):
    class Meta:
        model = models.Stabili


class StabiliView(mixins.ListModelMixin,
                  viewsets.GenericViewSet):

    queryset = models.Stabili.objects.all()
    serializer_class = SerializerStabili