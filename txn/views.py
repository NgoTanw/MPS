from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import auth,messages
from cards.models import CardList
from banks.models import BankList
from accounts.models import User
from txn.models import Transactions
from decimal import Decimal

def deposit(request):
	userdata = request.user
	cards = CardList.objects.all()
	banks = BankList.objects.all()
	if request.method == 'POST':
		username = userdata.username
		name = request.POST['name']
		card = request.POST['card']
		bank = request.POST['bank']
		deposit = Decimal(request.POST['deposit'])
		txns = Transactions.objects.create(to_account=username, from_account=username, name=name, card=card, bank=bank, txntype='Deposit', amount=deposit)
		txns.save()
		messages.success(request,'Amount Deposited. Balance will reflect after verification.')
		return redirect('deposit')
	return render(request, 'user/deposit.html', {'cards':cards, 'userdata':userdata,'banks':banks})

def withdraw(request):
	userdata = request.user
	cards = CardList.objects.all()
	banks = BankList.objects.all()
	if request.method == 'POST':
		username = userdata.username
		name = request.POST['name']
		card = request.POST['card']
		bank = request.POST['bank']
		withdraw = Decimal(request.POST['withdraw'])
		if withdraw < userdata.balance:
			txns = Transactions.objects.create(to_account=username, from_account=username, name=name, card=card, bank=bank, txntype='Withdraw', amount=withdraw)
			txns.save()
			messages.success(request,'Amount Withdrawn. Balance will reflect after verification.')
			return redirect('withdraw')
		else:
			messages.error(request,'Insufficient Balance')
			return redirect('withdraw')
	return render(request, 'user/withdraw.html', {'cards':cards, 'userdata':userdata,'banks':banks})

def transfer(request):
	current_user = request.user
	userdata = User.objects.all()
	cards = CardList.objects.all()
	banks = BankList.objects.all()
	if request.method == 'POST':
		username = current_user.username
		name = request.POST['name']
		card = request.POST['card']
		bank = request.POST['bank']
		to_account = request.POST['to_account']
		transfer = Decimal(request.POST['transfer'])
		if transfer < userdata.balance:
			txns = Transactions.objects.create(to_account=to_account, from_account=username, name=name, card=card, bank=bank, txntype='Transfer', amount=transfer)
			txns.save()
			messages.success(request,'Transfer Successful. Balance will reflect after verification.')
			return redirect('transfer')
		else:
			messages.error(request,'Insufficient Balance')
			return redirect('transfer')
	if current_user.is_staff:
		return render(request, 'vendor/transfer.html', {'cards':cards, 'current_user':current_user, 'userdata':userdata,'banks':banks})
	else:
		return render(request, 'user/transfer.html', {'cards':cards, 'current_user':current_user, 'userdata':userdata,'banks':banks})

def txnHistory(request):
	user = request.user
	txns = Transactions.objects.all()
	if user.is_superuser:
		return render(request, 'admin/transactions.html',{'txns': txns})
	elif user.is_staff and not user.is_superuser:
		return render(request, 'vendor/transactions.html',{'txns': txns})
	else:
		return render(request, 'user/transactions.html',{'txns': txns})

def txnVerify(request,id):
	txns = Transactions.objects.get(id=id)
	cards = CardList.objects.get(username=txns.from_account)
	from_acc = User.objects.get(username=txns.from_account)
	to_acc = User.objects.get(username=txns.to_account)
	if request.method == 'POST':
		pvtkey = request.POST['pvtkey']
		binary = request.POST['binary']
		if cards.pvtkey == pvtkey and cards.binary == binary:
			if txns.txntype == 'Deposit':
				to_acc.balance += txns.amount
				to_acc.save()
			elif txns.txntype == 'Withdraw':
				from_acc.balance -= txns.amount
				from_acc.save()
			elif txns.txntype == 'Transfer':
				to_acc.balance += txns.amount
				from_acc.balance -= txns.amount
				to_acc.save()
				from_acc.save()
			txns.txnstatus = True
			txns.save()
		return redirect('../transactions')
	return render(request, 'admin/verify.html', {'txns':txns})
