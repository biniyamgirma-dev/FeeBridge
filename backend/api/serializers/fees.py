from rest_framework import serializers
from fees.models import FeeStructure, Invoice

class FeeStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeStructure
        fields = '__all__'