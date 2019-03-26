from django.shortcuts import render
from .models import Trip, Country, Redactor, PlannedTrip
from django.views import generic


def index(request):
    """
    View function for home page of site.
    """

   # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html'
    )


# TRIP
class TripListView(generic.ListView):
    model = Trip
    ordering = 'title'
    # paginate_by = 10


# DAYS
class TripDetailView(generic.DetailView):
    model = Trip


# Redactors
class RedactorListView(generic.ListView):
    model = Redactor
    ordering = 'alias'
    # paginate_by = 10


class RedactorDetailView(generic.DetailView):
    model = Redactor


# Redactors
class CountryListView(generic.ListView):
    model = Country
    ordering = 'country_name'
    # paginate_by = 10


class CountryDetailView(generic.DetailView):
    model = Country


# TRIP PLANNING
class PlannedTripListView(generic.ListView):
    model = PlannedTrip
    ordering = 'title'
    # paginate_by = 10


# TRIP PLANNING STATUS UPDATE
class PlannedTripDetailView(generic.DetailView):
    model = PlannedTrip
