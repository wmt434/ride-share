from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

VEHICLE=(
	('a', 'type a'),
	('b', 'type b'),
	('c', 'type c'),
)


class Myuser(AbstractUser):
	email = models.EmailField(max_length=128)
	vehicle_type = models.CharField(max_length=1, choices=VEHICLE, default = 'a', blank=True)
	license_plate = models.CharField(max_length=10, default = 'None', blank=True)
	max_passenger = models.IntegerField(blank=True, default = 0)
	my_passenger = models.IntegerField(blank = True, default=0)
    # add additional fields in here
	#REQUIRED_FIELDS=['username', 'vehicle_type', 'license_plate', 'max_passenger']

	def get_absolute_url(self):
		#return reverse('current')
		return reverse('success-update')

	def __str__(self):
		return self.username


