from rest_framework import serializers
from fees.models import FeeStructure, Invoice

class FeeStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeStructure
        fields = '__all__'
      

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
        read_only_fields = ['amount']

    def create(self, validated_data):
        validated_data['amount'] = validated_data['fee_structure'].amount
        return super().create(validated_data)