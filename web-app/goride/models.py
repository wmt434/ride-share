from django.db import models
from django.utils import timezone
from users.models import Myuser
from django.urls import reverse


# Create your models here.
VEHICLE=(
	('a', 'type a'),
	('b', 'type b'),
	('c', 'type c'),
)

class Ride(models.Model):
	owner=models.ForeignKey(Myuser, on_delete=models.SET_NULL, 
		related_name='Owner', null=True)
	destination=models.CharField(max_length=128)
	required_arrival=models.DateTimeField(editable=True)
	number_of_owner_party=models.IntegerField()
	number_of_sharer_party = models.IntegerField(default=0)
	number_of_passenger = models.IntegerField(default=0)
	vehicle_type=models.CharField(
		max_length=1, choices=VEHICLE, blank=True,
	)
	Share_with_others = models.BooleanField(default=True)
	RIDE_STATUS = (
		('o', 'open'),
		('f', 'confirmed'),
		('c', 'completed')
	)
	status = models.CharField(
		max_length=1,
		choices=RIDE_STATUS,
		blank=True,
		default='o',
	)
	start_time = models.DateTimeField(default=timezone.now)
	driver = models.ForeignKey(Myuser, on_delete=models.SET_NULL,
	 related_name = 'Driver', null=True, blank = True)
	sharer = models.ForeignKey(Myuser, on_delete=models.SET_NULL,
	 null=True, related_name='Sharer', blank = True)

	class Meta:
		ordering=['start_time']
	def __str__(self):
		return f'ride {self.id}'
	
	def get_absolute_url(self):
		return reverse('ride-detail', kwargs={'pk': self.pk})
