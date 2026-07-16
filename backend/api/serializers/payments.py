from rest_framework import serializers
from payments.models import Payment, Receipt
from fees.models import StatusChoices


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['paid_by']

    def create(self, validated_data):
        validated_data['paid_by'] = self.context['request'].user
        payment = super().create(validated_data)

        invoice = payment.invoice
        invoice.status = StatusChoices.PAID
        invoice.save()

        Receipt.objects.create(
            payment=payment,
            receipt_number=f"RCP-{payment.id:06d}"
        )

        return payment