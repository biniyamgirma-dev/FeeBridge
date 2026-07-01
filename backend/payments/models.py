from django.db import models
from fees.models import Invoice
from accounts.models import User
class PaymentChoices(models.TextChoices):
    DIRECT = "DIRECT", "Direct"
    WALLET = "WALLET", "Wallet"

class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name="payments")
    paid_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=50, choices=PaymentChoices.choices, default=PaymentChoices.DIRECT)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.invoice} - {self.paid_by} - {self.amount}"
    
class Receipt(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name="receipt")
    receipt_number = models.CharField(max_length=50, unique=True)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.payment} - {self.receipt_number}"