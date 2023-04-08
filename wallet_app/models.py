from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class WalletUser(AbstractUser):
    email = models.EmailField(unique=True)


class Account(models.Model):
    bank = models.CharField(max_length=100, blank=False, null=False)
    account_name = models.CharField(max_length=255, blank=False, null=False)
    account_number = models.CharField(max_length=150, blank=False, null=False, unique=True)

    def __str__(self):
        return f'{self.bank}'


class CreditCard(models.Model):
    CREDIT_CARD_TYPE = [
        ("VERVE", "Verve"),
        ("MASTER CARD", 'Master Card'),
        ("VISA", "Visa")
    ]
    credit_card_type = models.CharField(max_length=20, choices=CREDIT_CARD_TYPE, default='Verve')
    card_number = models.CharField(max_length=16, blank=False, null=False)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3, blank=False, null=False)

    def __str__(self):
        return self.credit_card_type


class Wallet(models.Model):
    balance = models.DecimalField(default=0, max_digits=15, decimal_places=2)
    wallet_user = models.OneToOneField(WalletUser, on_delete=models.CASCADE, related_name='wallet')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='wallets')
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='wallets')

    def __str__(self):
        return f'{self.wallet_user} ({self.balance})'


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('TRANSFER', 'Transfer'),
        ('WITHDRAW', 'Withdraw'),
        ('DEPOSIT', 'Deposit'),
        ('AIRTIME', 'Airtime'),
        ('DATA', 'Data'),
        ('BILL', 'Bill')
    ]

    TRANSACTION_STATUS = [
        ('PENDING', 'Pending'),
        ('SENT', 'Sent'),
        ('FAILED', 'Failed')
    ]

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE, default='TRANSFER')
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='wallet_transactions')
    transaction_status = models.CharField(max_length=15, choices=TRANSACTION_STATUS, default='PENDING')
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_status


class Notification(models.Model):
    message = models.CharField(max_length=50, blank=False, null=False)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE, default='')
    wallet_user = models.OneToOneField(WalletUser, on_delete=models.CASCADE, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
