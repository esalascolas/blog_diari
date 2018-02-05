from django.shortcuts import render
from .models import Trip, Country, DayInstance, Redactor
from django.views import generic


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_trips = Trip.objects.count()
    num_days = DayInstance.objects.count()
    num_redactors = Redactor.objects.count()  # The 'all()' is implied by default.
    num_countries = Country.objects.count()
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_trips': num_trips,
            'num_redactors': num_redactors,
            'num_countries': num_countries,
            'num_days': num_days
        },
    )


# TRIP
class TripListView(generic.ListView):
    model = Trip
    paginate_by = 10


# DAYS
class TripDetailView(generic.DetailView):
    model = Trip


# Redactors
class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 10


class RedactorDetailView(generic.DetailView):
    model = Redactor


# Redactors
class CountryListView(generic.ListView):
    model = Country
    paginate_by = 10


class CountryDetailView(generic.DetailView):
    model = Country
