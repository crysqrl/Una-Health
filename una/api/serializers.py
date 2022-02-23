from rest_framework import serializers

from una.api.models import GlucoseData


class GlucoseDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = GlucoseData
        fields = '__all__'


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()
