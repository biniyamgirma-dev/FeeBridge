from rest_framework import serializers
from wallets.models import Wallet, WalletTransaction, TransactionChoices


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletTransaction
        fields = '__all__'
        read_only_fields = ['wallet', 'transaction_type']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['wallet'] = user.wallet
        validated_data['transaction_type'] = TransactionChoices.DEPOSIT
        transaction = super().create(validated_data)

        wallet = transaction.wallet
        wallet.balance += transaction.amount
        wallet.save()

        return transaction