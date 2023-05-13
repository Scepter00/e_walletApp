from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from wallet_app.models import *
from wallet_app.serializers import *


# Create your views here.
class CreateWallet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class AddAccount(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AddCreditCard(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CreditCardSerializer

