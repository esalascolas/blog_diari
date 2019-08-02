from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Trip, Redactor, Country, PlanStatusUpdate, PlannedTrip


# Pàgines estàtiques
class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['index', 'trips', 'redactors', 'countries', 'planned-trips']

    def location(self, item):
        return reverse(item)


# Pàquines dinàmiques
class TripSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Trip.objects.all()


# Pàquines dinàmiques
class RedactorSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Redactor.objects.all()


# Pàquines dinàmiques
class CountrySitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Country.objects.all()


# Pàquines dinàmiques
class PlannedTripSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return PlannedTrip.objects.all()


# Pàquines dinàmiques
class PlanStatusUpdateSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return PlanStatusUpdate.objects.all()




