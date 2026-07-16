from rest_framework.generics import CreateAPIView
from payments.models import Payment
from api.serializers.payments import PaymentSerializer
from rest_framework.permissions import IsAuthenticated


class PaymentCreateView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]