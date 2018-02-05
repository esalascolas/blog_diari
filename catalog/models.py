from django.db import models
from django.urls import reverse
import uuid


class Trip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    title = models.CharField(max_length=200)
    country = models.ManyToManyField('Country', help_text='Select a destiny')
    redactor = models.ManyToManyField('Redactor', help_text='Select redactor')
    summary = models.TextField(max_length=1000, help_text="Brief description of the trip")
    departure_date = models.DateField('departure',null=True, blank=True)
    arrival_date = models.DateField('arrival', null=True, blank=True)
    duration = models.IntegerField(help_text='Duration of the journey in days', default=0)
    route_trip_image = models.CharField(max_length=200, default='', help_text='Name of the image file saved in static ex: /images/trip.jpg')
    url_static = models.CharField(max_length=200, default='', help_text='Route from the static folder ex (/static) /marroc (Just the /marroc)')
    LOAN_STATUS = (
        ('e', 'Eye on it'),
        ('p', 'Planed'),
        ('o', 'On voyage'),
        ('d', 'Done'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='e', help_text='Status of the trip')

    def __str__(self):
        return self.title

    @property
    def duration_calc(self):
        if self.duration == 0 and self.departure_date is not None and self.arrival_date is not None:
            total = self.departure_date-self.arrival_date
        elif self.duration is not None:
            total = self.duration
        else:
            total = 0
        return total

    def get_absolute_url(self):
        return reverse('trip-detail', args=[str(self.id)])

    def display_country(self):
        return ', '.join([country.country_name for country in self.country.all()[:3]])

    def display_redactor(self):
        return ', '.join([redactor.alias for redactor in self.redactor.all()[:3]])

    display_country.short_description = 'Country'


class DayInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    title = models.CharField(max_length=50, help_text='Day title')
    travel = models.ForeignKey('Trip', on_delete=models.SET_NULL, null=True)
    departure_date = models.DateField('departure', null=True, blank=True)
    arrival_date = models.DateField('arrival', null=True, blank=True)
    duration = models.IntegerField(help_text='Duration of the journey in days')
    description = models.TextField(max_length="5000")

    def __str__(self):
        return self.title

    @property
    def duration_calc(self):
        if self.duration == 0:
            total = self.departure_date - self.arrival_date
        else:
            total = self.duration
        return total


class Redactor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)
    date_of_birth = models.DateField('Birth: ', null=True, blank=True)
    description = models.CharField(max_length=5000, help_text='Presentet: edat, qui ets? Que busques fer amb aquest blog? Què tagrada...', default='')

    def __str__(self):
        return self.alias

    def get_absolute_url(self):
        return reverse('redactor-detail', args=[str(self.id)])

    class Meta:
        ordering = ["last_name", "first_name"]


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=3)
    url_imatge_bandera = models.CharField(max_length=500, default="")

    def __str__(self):
        return '{0}, {1}'.format(self.country_name, self.country_code)

    def get_absolute_url(self):
        return reverse('country-detail', args=[str(self.id)])
