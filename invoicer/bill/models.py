from django.db import models
from django.utils import timezone 

class Bill(models.Model):
	invoice = models.CharField(max_length=100)
	buyer_name = models.CharField(max_length=50)
	buyer_address = models.CharField(max_length=150)
	buyer_gstin = models.CharField(max_length=15)
	buyer_mobile = models.CharField(max_length=10)
	date_of_issue = models.DateField()
	total = models.FloatField(default=0)
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
	rate = models.FloatField()
	discount = models.FloatField()
	taxable_value = models.FloatField()
	cgst_rate = models.IntegerField()
	cgst_amount = models.FloatField()
	sgst_rate = models.IntegerField()
	sgst_amount = models.FloatField()
	igst_rate = models.IntegerField()
	igst_amount = models.FloatField()
	amount = models.FloatField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "{} {} {}".format(self.bill, self.description, self.amount)