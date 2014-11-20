from rest_framework import serializers, mixins, permissions, viewsets
import models


class SerializerPosti(serializers.ModelSerializer):
    class Meta:
        model = models.Posti


class PostiView(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):

    queryset = models.Posti.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = SerializerPosti

    def get_queryset(self):
        return models.Posti.get_posti_recenti()
