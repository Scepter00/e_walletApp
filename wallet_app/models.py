from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class WalletUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, max_length=15, null=True)
    profile_image = models.ImageField(upload_to='media/images', default=None)


class Account(models.Model):
    bank = models.CharField(max_length=255, null=False, blank=False)
    account_number = models.CharField(max_length=10)

    def __str__(self):
        return self.bank


class Card(models.Model):
    card_number = models.CharField(max_length=16, blank=False, null=False)
    card_name = models.CharField(max_length=255)
    expiry_date = models.DateField()
    cvv = models.CharField(max_length=3, blank=False, null=False)

    def __str__(self):
        return self.card_name


class Beneficiary(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='beneficiaries', null=True, blank=True)

    def __str__(self):
        return str(self.account)


class Transaction(models.Model):
    TRANSACTION_TYPE = [
        ('TRANSFER', 'Transfer'),
        ('WITHDRAW', 'Withdraw'),
        ('DEPOSIT', 'Deposit'),
        ('AIRTIME', 'Airtime'),
        ('DATA', 'Data'),
        ('BILL', 'Bill')
    ]

    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='transactions', default=None)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE, default='TRANSFER')
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_type


class Wallet(models.Model):
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    wallet_user = models.OneToOneField(WalletUser, on_delete=models.CASCADE, related_name='wallet')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='wallets')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='wallets',default=None )
    beneficiary = models.ForeignKey(Beneficiary, on_delete=models.CASCADE, related_name='wallets', null=True, blank=True, )
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='wallets', default=None)

    def __str__(self):
        return str(self.wallet_user)
