from rest_framework.generics import CreateAPIView
from wallets.models import WalletTransaction
from api.serializers.wallets import DepositSerializer
from rest_framework.permissions import IsAuthenticated


class DepositView(CreateAPIView):
    queryset = WalletTransaction.objects.all()
    serializer_class = DepositSerializer
    permission_classes = [IsAuthenticated]