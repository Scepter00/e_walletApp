from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class WalletUser(AbstractUser):
    email = models.EmailField(unique=True)


class Account(models.Model):
    bank = models.CharField(max_length=100, blank=False, null=False)
    account_name = models.CharField(max_length=255, blank=False, null=False)
    account_number = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return f'{self.bank} {self.account_name}'


class CreditCard(models.Model):
    CREDIT_CARD_TYPE = [
        ("VERVE", "VER"),
        ("MASTER CARD", 'Master Card'),
        ("VISA", "Visa")
    ]
    credit_card_type = models.CharField(max_length=20, choices=CREDIT_CARD_TYPE, default='')
    card_number = models.IntegerField
    expiry_date = models.DateField(blank=False, null=False)
    cvv = models.IntegerField

    def __str__(self):
        return self.CREDIT_CARD_TYPE


class Wallet(models.Model):
    balance = models.DecimalField(default=0, max_digits=15, decimal_places=4)
    wallet_user = models.OneToOneField(WalletUser, on_delete=models.CASCADE, default='')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='accounts')
    credit_card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name='credit_cards')

    def __str__(self):
        return self.wallet_user


class Beneficiary(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, default='')

    def __str__(self):
        pass


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('TRANSFER', 'Transfar'),
        ('WITHDRAW', 'Withdraw'),
        ('DEPOSIT', 'Deposit'),
        ('AIRTIME', 'Airtime'),
        ('DATA', 'Data'),
        ('BILL', 'Bill')
    ]

    TRANSACTION_STATUS = [
        ('PENDNG', 'Pending'),
        ('SENT', 'Sent'),
        ('FAILED', 'Failed')
    ]

    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE, default='Select')
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='wallet_transactions')
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name='beneficiary_transaction')
    transaction_status = models.CharField(max_length=15, choices=TRANSACTION_STATUS)
    transaction_date = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.transaction_status


class Notification(models.Model):
    message = models.CharField(max_length=50, blank=False, null=False)
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE, default='')
    wallet_user = models.OneToOneField(WalletUser, on_delete=models.CASCADE, default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
