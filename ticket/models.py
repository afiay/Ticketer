from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from guardian.shortcuts import assign_perm



# Create your models here.
class Ticket(models.Model):
	urgency_choices = [
		(1, '1'),
		(2, '2'),
		(3, '3'),
		(4, '4'),
		(5, '5'),
		(6, '6'),
		(7, '7'),
		(8, '8'),
		(9, '9'),
		(10, '10'),
	]

	ticket_type_choices = [
		('Tracksys', 'Tracksys'),
        ('AHL', 'AHL'),
		('Stative','Stative'),
        ('Compact', 'Compact'),
		('Pack & Plock', 'Pack & Plock'),
		('DelMontage', 'DelMontage'),
    ]
	
	ticket_status = [
	    ('N', 'Ny'),
	    ('O', 'Oppet'),
	    ('J', 'Jobbar'),
	    ('S', 'Stängd'),
	]
	ticket_location = [
	    ('ALL', 'ALL'),
	    ('Logistics_1', 'Logistics_2'),
	    ('Logistics_2', 'Logistics_3'),
	    ('Logistics_3', 'Logistics_4'),
	    ('Logistics_4', 'Logistics_5'),
	    ('AHL_station_2', 'Ahl_station_3'),
	    ('Ahl_station_3', 'Ahl_station_4'),
	    ('Ahl_station_4', 'Ahl_station_5'),
		('Stative_station_0', 'Stative_station_0'),
	    ('Stative_station_1', 'Stative_station_1'),
	    ('Stative_station_2', 'Stative_station_2'),
	    ('Stative_station_3', 'Stative_station_3'),
	    ('Stative_station_4', 'Stative_station_4'),
	    ('1000_station_0', '1000_station_0'),
	    ('1000_station_1', '1000_station_1'),
	    ('1000_station_2', '1000_station_2'),
	    ('1000_station_3', '1000_station_3'),
	    ('1000_station_4', '1000_station_4'),
		('Compact_station_0', 'Compact_station_0'),
		('Compact_station_1', 'Compact_station_1'),
	    ('Compact_station_2', 'Compact_station_2'),
	    ('Compact_station_3', 'Compact_station_3'),
	    ('Compact_station_4', 'Compact_station_4'),
	    ('Pack&plock_0', 'Pack&plock_0'),
	    ('Pack&plock_1', 'Pack&plock_1'),
	    ('Pack&plock_2', 'Pack&plock_2'),
	    ('Pack&plock_3', 'Pack&plock_3'),
	    ('Pack&plock_4', 'Pack&plock_4'),
	    ('Del_Montage_0', 'Del_Montage_0'),
	    ('Del_Montage_1', 'Del_Montage_1'),
	    ('Del_Montage_2', 'Del_Montage_2'),
	    ('Del_Montage_3', 'Del_Montage_3'),
	    ('Del_Montage_4', 'Del_Montage_4'),
	] 

	title = models.CharField(max_length=100, verbose_name='Ar Nummer / Plockplats')
	ticket_location = models.CharField(max_length=36, choices=ticket_location, default='0')
	image = models.ImageField(upload_to='media/images', blank=True)
	content = models.TextField()
	date_ticketed = models.DateTimeField(default=timezone.now)
	status = models.CharField(max_length=1, choices=ticket_status, default='N')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	ticket_type = models.CharField(max_length=50, default='Tracksys', choices=ticket_type_choices)
	urgency = models.IntegerField(
		default=1, 
		validators=[MinValueValidator(1), MaxValueValidator(10)], 
		verbose_name='Brotskande (1-10)',
		error_messages={'max_value': 'Välj ett brådskande mellanrum 1 och 10', 'min_value': 'Välj ett brådskande mellanrum 1 och 10'})
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('ticket-detail', kwargs={'pk': self.pk})

Ticket.objects.order_by('-urgency')

@receiver(post_save, sender=Ticket)
def set_permission(sender, instance, **kwargs):
	assign_perm("view_ticket", instance.author, instance)
	group = Group.objects.get(name='Ticketing Staff')
	assign_perm("view_ticket", group, instance)
	assign_perm("change_ticket", group, instance)
	assign_perm("delete_ticket", group, instance)

class Replie(models.Model):
	ticket = models.ForeignKey(Ticket, related_name="replies", on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	replier = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	date_replied = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '%s - %s' % (self.ticket.title, self.name)

	def get_absolute_url(self):
		return reverse('ticket-home')