from django.db import models

class Bill(models.Model):
	invoice = models.CharField(max_length=100)
	buyer_name = models.CharField(max_length=50)
	buyer_address = models.CharField(max_length=150)
	buyer_gstin = models.CharField(max_length=15)
	buyer_mobile = models.CharField(max_length=10)
	date_of_issue = models.DateField()
	total = models.DecimalField(max_digits = 10, decimal_places = 2)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "id: {}, {}, {}".format(self.id, self.input_name, self.date_of_issue)


class Product(models.Model):
	bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
	description = models.CharField(max_length=100)
	item_type = models.CharField(max_length=100)
	hsn = models.IntegerField()
	quantity = models.IntegerField()
	rate = models.DecimalField(max_digits = 10, decimal_places = 2)
	discount = models.DecimalField(max_digits = 10, decimal_places = 2)
	taxable_value = models.DecimalField(max_digits = 10, decimal_places = 2)
	cgst_rate = models.DecimalField(max_digits = 10, decimal_places = 2)
	cgst_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
	sgst_rate = models.DecimalField(max_digits = 10, decimal_places = 2)
	sgst_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
	igst_rate = models.DecimalField(max_digits = 10, decimal_places = 2)
	igst_amount = models.DecimalField(max_digits = 10, decimal_places = 2)
	amount = models.DecimalField(max_digits = 10, decimal_places = 2)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{} {} {}".format(self.bill, self.description, self.amount)