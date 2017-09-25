from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Bill, Product, Profile, PLACES

class DateInput(forms.DateInput):	#Used for the dateinput widget
	input_type = 'date'
	format = '%d/%m/%y'


class ProfileForm(UserCreationForm):
	first_name = forms.CharField(max_length = 30)
	last_name = forms.CharField(max_length = 30)
	email = forms.EmailField(max_length = 254, help_text = 'Required. Inform a valid email address.')
	company = forms.CharField(max_length = 50)
	address = forms.CharField(widget = forms.Textarea)
	mobile = forms.CharField(max_length = 10)
	gstin = forms.CharField(max_length = 15)
	place_of_supply = forms.ChoiceField(choices = PLACES)

	class Meta:
		model = User
		fields = ('username', 
    			  'password1', 
    			  'password2', 
    			  'first_name', 
    			  'last_name',
    			  'email', 
    			  'company', 
    			  'mobile',
    			  'gstin',
    			  'place_of_supply',)


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