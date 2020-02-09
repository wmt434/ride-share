from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Myuser

VEHICLE=(
	('a', 'type a'),
	('b', 'type b'),
	('c', 'type c'),
)

class RiderRegisterForm(UserCreationForm):

	class Meta:
		model = Myuser
		fields = ['username', 'email','password1', 'password2']


class DriverRegisterForm(UserCreationForm):
	vehicle_type = forms.ChoiceField(choices=VEHICLE, required=True)
	license_plate = forms.CharField(max_length=10, required=True)
	max_passenger = forms.IntegerField(required=True)

	class Meta:
		model = Myuser
		fields = ['username', 'email', 'vehicle_type', 'license_plate',
        'max_passenger', 'password1', 'password2']
