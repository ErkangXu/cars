from django.contrib import admin

from .models import Customer
from .models import Car
from .models import Reservation
from .models import Violation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
	search_fields = ['customer__name', 'car__car_name']
	list_filter = ('security_deposit_return',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	search_fields = ['name', 'ID_number']

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
	search_fields = ['plateName', 'car_name']

@admin.register(Violation)
class ViolationAdmin(admin.ModelAdmin):
	search_fields = ['violator__name', 'car__car_name']
