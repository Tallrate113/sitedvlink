from rest_framework import serializers
from .models import *
class ApplicationsSerializer(serializers.Serializer):
    field_organisation_name = serializers.CharField(max_length=255)
    field_text_appeal = serializers.CharField(max_length=255)
    stat_id = serializers.IntegerField()
    emp_id = serializers.IntegerField()
    field_number_phone = serializers.CharField(max_length=18)
    field_email = serializers.EmailField(max_length=255)
    field_fio = serializers.CharField(max_length=255)
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Applications.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.field_text_appeal = validated_data.get("field_text_appeal", instance.field_text_appeal)
        instance.save()
        return instance
