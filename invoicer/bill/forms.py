from django import forms
from .models import Bill, Product

class DateInput(forms.DateInput):	#Used for the dateinput widget
	input_type = 'date'
	format = '%d/%m/%y'


class BillForm(forms.ModelForm):
	class Meta:
		model = Bill
		fields = ['buyer_name',
				  'buyer_address',
				  'buyer_gstin',
				  'buyer_mobile',
				  'date_of_issue',]
		widgets = {
			'date_of_issue': DateInput(),
		}


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['description',
				  'item_type',
				  'hsn',
				  'quantity',
				  'rate',
				  'discount',
				  'cgst_rate',
				  'sgst_rate',
				  'igst_rate',]