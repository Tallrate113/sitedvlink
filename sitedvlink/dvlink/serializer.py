from rest_framework import serializers
from .models import *


class ApplicationsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Applications
        fields = ("field_organisation_name", "field_text_appeal", "stat", "field_number_phone", "field_email",
                  "field_fio", "time_create", "time_update", "user")
