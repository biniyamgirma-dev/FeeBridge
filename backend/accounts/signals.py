from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from wallets.models import Wallet


@receiver(post_save, sender=User)
def create_wallet_for_new_user(sender, instance, created, **kwargs):
    if created and instance.role == 'PARENT':
        Wallet.objects.create(parent=instance)