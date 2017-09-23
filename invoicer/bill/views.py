from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import View
from .models import Bill, Product
from .forms import BillForm, ProductForm

@login_required
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
			id = bill.id
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
		bill.invoice = "IN{0}Z{1}".format(bill.date_of_issue.strftime("%y%m%d"), bill.id)
		add_product.bill = bill
		add_product.save()
		bill.save()
		return redirect('bill:products', id)

	context = {
		'bill': bill,
		'products': products,
		'add_product': add_product	}
	return render(request, 'bill/new_product.html', context)


def history(request):
	bills = Bill.objects.all().order_by('-created')
	return render(request, 'bill/history.html', { 'bills': bills })