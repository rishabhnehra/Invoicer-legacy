from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic import View
from .models import Bill, Product, Profile
from .forms import BillForm, ProductForm, ProfileForm

def signup(request):
	form = ProfileForm(request.POST or None)
	if form.is_valid():
		user = form.save()
		user.refresh_from_db()
		user.profile.company = form.cleaned_data.get('company')
		user.profile.mobile = form.cleaned_data.get('mobile')
		user.profile.gstin = form.cleaned_data.get('gstin')
		user.profile.address = form.cleaned_data.get('address')
		user.profile.place_of_supply = form.cleaned_data.get('place_of_supply')
		user.save()
		raw_password = form.cleaned_data.get('password1')
		user = authenticate(username = user.username, password = raw_password)
		login(request, user)
		return redirect('bill:dashboard')
	return render(request, 'registration/signup.html', { 'form': form })

@login_required
def dashboard(request):		#Shows the list of all the stored bills
	bills = Bill.objects.filter(user = request.user).order_by('-created')[:10]
	return render(request, 'bill/dashboard.html', { 'bills': bills })

@login_required
def detail_new(request, id):	#A detail view of that Bill id
	bill = get_object_or_404(Bill, id=id)
	user = request.user
	print(user)
	products = bill.product_set.all()
	context = {
		'bill': bill,
		'products': products,
		'user': user
	}
	return render(request, 'bill/summary_new.html', context)

@login_required
def detail(request, id):	#A detail view of that Bill id
	bill = get_object_or_404(Bill, id=id)
	user = request.user
	print(user)
	products = bill.product_set.all()
	context = {
		'bill': bill,
		'products': products,
		'user': user
	}
	return render(request, 'bill/summary.html', context)

@login_required
def new_bill(request):
	bill = BillForm(request.POST or None)
	if bill.is_valid():
			new_bill = bill.save(commit = False)
			new_bill.user = request.user
			new_bill.save()
			return redirect('bill:products', new_bill.id)
	return render(request, 'bill/new_bill.html', { 'bill': bill })

@login_required
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

@login_required
def history(request):
	bills = Bill.objects.filter(user = request.user).order_by('-created')
	return render(request, 'bill/history.html', { 'bills': bills })