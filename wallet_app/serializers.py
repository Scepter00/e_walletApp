from rest_framework import serializers

from wallet_app.models import *

from djoser.serializers import UserCreateSerializer


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['balance', 'wallet_user']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['bank', 'account_name', 'account_number']


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['credit_card_type', 'card_number', 'expiry_date', 'cvv']
        expiry_date = serializers.DateField(read_only=True)


class UserCreate(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'phone']
