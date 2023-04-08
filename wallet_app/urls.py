from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views

router = DefaultRouter()
router.register('wallet', views.CreateWallet)
router.register('account', views.AddAccount)
router.register('card', views.AddCreditCard)

urlpatterns = [
    path('', include(router.urls))
]
