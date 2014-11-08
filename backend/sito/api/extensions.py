from rest_framework import viewsets


class MultiSerializer(viewsets.GenericViewSet):
    """
    Allows to use different serializers according to
    the action which is being taken.
    """
    serializer_mapping = {}
    default_serializer = None

    def get_serializer_class(self):
        return self.serializer_mapping.get(self.action,
                                           self.default_serializer)


class MultiPermissions(viewsets.GenericViewSet):
    permission_mapping = {}
    default_permissions = None

    def check_permissions(self, request):
        permission_class = self.permission_mapping.get(self.action,
                                                       self.default_permissions)

        if not permission_class().has_permission(request, self):
            self.permission_denied(request)