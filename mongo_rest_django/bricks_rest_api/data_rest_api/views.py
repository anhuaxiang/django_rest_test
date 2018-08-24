from rest_framework_mongoengine import viewsets
from data_rest_api.serializers import ToolSerializer
from data_rest_api.models import Tool
from rest_framework import permissions


class ToolViewSet(viewsets.ModelViewSet):
    """
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    """
    lookup_field = 'id'
    serializer_class = ToolSerializer
    queryset = Tool.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

