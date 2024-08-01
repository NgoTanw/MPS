from django.urls import path
from . import views

urlpatterns = [
	path('deposit',views.deposit, name="deposit"),
	path('withdraw',views.withdraw, name="withdraw"),
	path('transfer',views.transfer, name="transfer"),
	path('transactions',views.txnHistory, name="txnHistory"),
	path('verification/<int:id>',views.txnVerify, name="txnVerify"),
]
