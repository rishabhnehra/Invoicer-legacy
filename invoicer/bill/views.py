from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View
from twilio.rest import Client
from .models import Bill, Product
from .forms import BillForm, ProductForm


def dashboard(request):		#Shows the list of all the stored bills
	bills = Bill.objects.all().order_by('-created')[:10]
	context = {
		'bills': bills
	}
	return render(request, 'bill/dashboard.html', context)


def detail(request, id):	#A detail view of that Bill id
	bill = get_object_or_404(Bill, id=id)
	products = bill.product_set.all()
	context = {
		'bill': bill,
		'products': products
	}
	return render(request, 'bill/summary.html', context)


def new_bill(request):
	bill = BillForm(request.POST or None)
	if bill.is_valid():
			bill = bill.save()
			return redirect('bill:products', bill.id)
	context = {
		'bill': bill
	}
	return render(request, 'bill/new_bill.html', context)


def products(request, id):
	bill = get_object_or_404(Bill, id=id)
	products = bill.product_set.all()
	add_product = ProductForm(request.POST or None)
	if add_product.is_valid():
		add_product = add_product.save(commit=False)
		add_product.taxable_value = add_product.rate * add_product.quantity
		if add_product.discount > 0:
			add_product.taxable_value = add_product.taxable_value - (add_product.taxable_value*(add_product.discount/100))
		add_product.cgst_amount = add_product.taxable_value * (float(add_product.cgst_rate)/100)
		add_product.sgst_amount = add_product.taxable_value * (float(add_product.sgst_rate)/100)
		add_product.igst_amount = add_product.taxable_value * (float(add_product.igst_rate)/100)
		if add_product.igst_amount != 0:
			add_product.amount = add_product.taxable_value + add_product.igst_amount
		else:
			add_product.amount = add_product.taxable_value + add_product.cgst_amount + add_product.sgst_amount
		bill.total = bill.total + add_product.amount
		bill.invoice = "RC{0}9{1}".format(bill.date_of_issue.strftime("%y%m%d"), bill.id)
		add_product.bill = bill
		add_product.save()
		bill.save()
		return redirect('bill:products', id)

	context = {
		'bill': bill,
		'products': products,
		'add_product': add_product	}
	return render(request, 'bill/new_product.html', context)


def send_sms(request, id):
	print("YO")
	bill = get_object_or_404(Bill, id = id)
	to = "+91{0}".format(bill.buyer_mobile)
	message = "Your invoice no. is {}. And the amount payable is ₹{}".format(bill.invoice, bill.total)
	account_sid = os.environ['TWILIO_ACCOUNT_SID']
	auth_token = os.environ['TWILIO_AUTH_TOKEN']
	client = Client(account_sid, auth_token)
	print("Object Created")
	
	try:
		client.messages.create(
		    to = to,
		    from_ = os.environ['TWILIO_NUMBER'],
		    body = message
	    )
	except Exception as e:
		print(e)

	print("Passed the send_sms")
	return redirect('bill:summary', id)


def history(request):
	bills = Bill.objects.all().order_by('-created')
	return render(request, 'bill/history.html', { 'bills': bills })