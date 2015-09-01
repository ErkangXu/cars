from django.db import models
import json

class Car(models.Model):
	car_name = models.CharField(max_length=100)
	make = models.CharField(max_length=50)
	engine_identification=models.CharField(max_length=20)
	color=models.CharField(max_length=50)
	plateName=models.CharField(max_length=50)
	def __str__(self):
		return self.car_name

class Reservation(models.Model):
	PAYMENT_TYPE_CHOICES = (
		('CASH', 'Cash'),
		('CARD', 'Card'),
	)
	customer = models.ForeignKey('Customer')
	car = models.ForeignKey('Car')
	startDate = models.DateField()
	endDate = models.DateField()
	total_amount = models.IntegerField()
	security_deposit_return = models.BooleanField()
	payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICES)
	def __str__(self):
		return str(self.car)+'|'+str(self.customer)+'|'+str(self.startDate)+'~'+str(self.endDate)
	def to_JSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class Customer(models.Model):
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
	)
	name = models.CharField(max_length=100)
	birth_day = models.DateField()
	gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
	license_number = models.CharField(max_length=50)
	ID_number = models.CharField(max_length=60)
	hometown = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=20)
	def __str__(self):
		return self.name+str(self.birth_day)


class Violation(models.Model):
	car = models.ForeignKey('Car')
	location = models.CharField(max_length=50)
	violator = models.ForeignKey('Customer')
	date = models.DateField()
	kind = models.CharField(max_length=30)
	fine = models.IntegerField()
	points = models.IntegerField()
	note = models.TextField()
	handled = models.BooleanField()
	def __str__(self):
		return str(self.car)+str(self.violator)+str(self.date)