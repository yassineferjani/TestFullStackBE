from rest_framework import serializers
from .models import jsondoc


class jsondocSerializer(serializers.Serializer):
    class Meta:
        model: jsondoc
        fields: ['id', 'text']
