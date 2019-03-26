from django.db import models
from django.urls import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static


# Instància viatge
class Trip(models.Model):
    title = models.CharField(max_length=200)
    country = models.ManyToManyField('Country', help_text='Selecciona un destí')
    redactor = models.ManyToManyField('Redactor', help_text='Selecciona un redactor')
    summary = models.TextField(max_length=1000)
    departure_date = models.DateField('departure', null=True, blank=True)
    arrival_date = models.DateField('arrival', null=True, blank=True)
    duration = models.IntegerField(help_text='Durada del viatge en dies', default=0)
    route_trip_image = models.CharField(max_length=200, default='', help_text='Nom de la imatge guardada a la carpeta static ex: /images/trip.jpg')
    url_static = models.CharField(max_length=200, default='', help_text='Ruta a la carpeta /static ex: de "/static/marroc" només "/marroc"')
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

    def get_image_url(self):
        return static(self.route_trip_image)

    def get_hero_url(self):
        return static('images' + self.url_static + '/hero.jpg')

    def display_country(self):
        return ', '.join([country.country_name for country in self.country.all()[:3]])

    def display_redactor(self):
        return ', '.join([redactor.alias for redactor in self.redactor.all()[:3]])

    display_country.short_description = 'Country'


# Instància dia
class DayInstance(models.Model):
    title = models.CharField(max_length=50, help_text='Titol del dia')
    travel = models.ForeignKey('Trip', on_delete=models.SET_NULL, null=True)
    departure_date = models.DateField('departure', null=True, blank=True)
    arrival_date = models.DateField('arrival', null=True, blank=True)
    duration = models.IntegerField(help_text='Durada del viatge en dies')
    description = models.TextField(max_length="5000")
    day_image = models.ImageField(upload_to='day', blank=True)

    def __str__(self):
        return self.title

    @property
    def duration_calc(self):
        if self.duration == 0:
            total = self.departure_date - self.arrival_date
        else:
            total = self.duration
        return total

    @property
    def image_url(self):
        if self.day_image and hasattr(self.day_image, 'url'):
            return self.day_image.url


# Classe redactor
class Redactor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    alias = models.CharField(max_length=50)
    date_of_birth = models.DateField('Birth: ', null=True, blank=True)
    description = models.TextField(max_length=5000, default="")

    def __str__(self):
        return self.alias

    def get_absolute_url(self):
        return reverse('redactor-detail', args=[str(self.id)])

    def get_image_url(self):
        return static('images/' + self.alias.lower() + ".jpg")

    def get_hero_url(self):
        return static('images/' + self.alias.lower() + '/hero.jpg')

    class Meta:
        ordering = ["last_name", "first_name"]


# Classe pais
class Country(models.Model):
    country_name = models.CharField(max_length=100, default="")
    country_code = models.CharField(max_length=3, default="")
    url_imatge_bandera = models.CharField(max_length=500, default="")
    description = models.CharField(max_length=1500, default="")
    currency = models.CharField(max_length=30, default="")
    currency_sign = models.CharField(max_length=15, default="")
    cant_miss = models.CharField(max_length=300, default="")
    traditional_food = models.CharField(max_length=300, default="")
    flag_image = models.ImageField(upload_to='country', default="")

    def __str__(self):
        return '{0}, {1}'.format(self.country_name, self.country_code)

    def get_absolute_url(self):
        return reverse('country-detail', args=[str(self.id)])


# Classe planificació de viatges
class PlannedTrip(models.Model):
    title = models.CharField(max_length=200)
    country = models.ManyToManyField('Country', help_text='Selecciona un destí')
    voyagers = models.ManyToManyField('Redactor', help_text='Escolleix a un viatger')
    summary = models.TextField(max_length=1000)
    departure_date = models.DateField('departure', null=True, blank=True)
    arrival_date = models.DateField('arrival', null=True, blank=True)
    duration = models.IntegerField(help_text='Durada del viatge en dies (aprox)', default=0)
    route_trip_image = models.CharField(max_length=200, default='',
                                        help_text='Nom de la imatge guardada a la carpeta static ex: /images/trip.jpg')
    url_static = models.CharField(max_length=200, default='',
                                  help_text='Ruta a la carpeta /static ex: de "/static/marroc" només "/marroc"')
    LOAN_STATUS = (
        ('e', 'Eye on it'),
        ('p', 'Planed'),
        ('o', 'On voyage'),
        ('d', 'Done'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='e',
                              help_text='Status of the trip')

    def __str__(self):
        return self.title

    @property
    def duration_calc(self):
        if self.duration == 0 and self.departure_date is not None and self.arrival_date is not None:
            total = self.departure_date - self.arrival_date
        elif self.duration is not None:
            total = self.duration
        else:
            total = 0
        return total

    def get_absolute_url(self):
        return reverse('planned-trip-detail', args=[str(self.id)])

    def get_image_url(self):
        return static(self.route_trip_image)

    def get_hero_url(self):
        return static('images/' + self.url_static + '/hero.jpg')

    def display_country(self):
        return ', '.join([country.country_name for country in self.country.all()[:3]])

    def display_redactor(self):
        return ', '.join([redactor.alias for redactor in self.voyagers.all()[:3]])

    display_country.short_description = 'Country'


# Instància dia
class PlanStatusUpdate(models.Model):
    title = models.CharField(max_length=50, help_text='Titol de l\'actualització')
    travel = models.ForeignKey('PlannedTrip', on_delete=models.SET_NULL, null=True)
    update_date = models.DateField('updateDate', null=True, blank=True)
    description = models.TextField(max_length="5000")
    day_image = models.ImageField(upload_to='day', blank=True)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.day_image and hasattr(self.day_image, 'url'):
            return self.day_image.url
