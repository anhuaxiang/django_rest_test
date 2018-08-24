from rest_framework_mongoengine import serializers
from data_rest_api.models import Tool


class ToolSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Tool
        fields = '__all__'
