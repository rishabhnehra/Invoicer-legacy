from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone 

PLACES = (
	(1, 'Jammu & Kashmir'),
	(2, 'Himachal Pradesh'),
	(3, 'Punjab'),
	(4, 'Chandigarh'),
	(5, 'Uttarakhand'),
	(6, 'Haryana'),
	(7, 'Delhi'),
	(8, 'Rajasthan'),
	(9, 'Uttar Pradesh'),
	(10, 'Bihar'),
	(11, 'Sikkim'),
	(12, 'Arunachal Pradesh'),
	(13, 'Nagaland'),
	(14, 'Manipur'),
	(15, 'Mizoram'),
	(16, 'Tripura'),
	(17, 'Meghalaya'),
	(18, 'Assam'),
	(19, 'West Bengal'),
	(20, 'Jharkhand'),
	(21, 'Odisha'),
	(22, 'Chhattisgarh'),
	(23, 'Madhya Pradesh'),
	(24, 'Gujarat'),
	(25, 'Daman & Diu'),
	(26, 'Dadra & Nagar Haveli'),
	(27, 'Maharashtra'),
	(29, 'Karnataka'),
	(30, 'Goa'),
	(31, 'Lakshdweep'),
	(32, 'Kerala'),
	(33, 'Tamil Nadu'),
	(34, 'Pondicherry'),
	(35, 'Andaman & Nicobar Island'),
	(36, 'Telangana'),
	(37, 'Andhra Pradesh'),
	(97, 'Other Territory')
)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	company = models.CharField(max_length = 50)
	mobile = models.CharField(max_length = 10)
	gstin = models.CharField(max_length = 15)
	place_of_supply = models.CharField(choices = PLACES, max_length = 30)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()


class Bill(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	invoice = models.CharField(max_length = 100)
	buyer_name = models.CharField(max_length = 50)
	buyer_address = models.CharField(max_length = 150)
	buyer_gstin = models.CharField(max_length = 15)
	buyer_mobile = models.CharField(max_length = 10)
	date_of_issue = models.DateField()
	total = models.FloatField(default = 0)
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "id: {}, {}, {}".format(self.id, self.input_name, self.date_of_issue)


class Product(models.Model):
	bill = models.ForeignKey(Bill, on_delete = models.CASCADE)
	description = models.CharField(max_length = 100)
	item_type = models.CharField(max_length = 100)
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
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "{} {} {}".format(self.bill, self.description, self.amount)