from rest_framework import serializers
from app.models import Port

class PortSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Port
        fields = ["id", "code","name"]
        ref_name = "Admin_Port"