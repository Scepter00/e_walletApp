from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.
@admin.register(WalletUser)
class User(UserAdmin):
    pass


admin.site.register(Account)
admin.site.register(Wallet)
admin.site.register(CreditCard)
admin.site.register(Transaction)
admin.site.register(Notification)
