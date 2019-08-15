from django.urls import path, include
from . import views
from .sitemaps import *
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'trip': TripSitemap(),
    'redactor': RedactorSitemap(),
    'country': CountrySitemap(),
    'planned-trips': PlannedTripSitemap(),
    'static': StaticSitemap(),
}


urlpatterns = [
    path('', views.index, name='index'),
    path('trips/', views.TripListView.as_view(), name='trips'),
    path('trips/<int:pk>', views.TripDetailView.as_view(), name='trip-detail'),
    path('writers/', views.RedactorListView.as_view(), name='redactors'),
    path('writers/<str:pk>', views.RedactorDetailView.as_view(), name='redactor-detail'),
    path('countries/', views.CountryListView.as_view(), name='countries'),
    path('countries/<str:pk>', views.CountryDetailView.as_view(), name='country-detail'),
    path('planned-trips/', views.PlannedTripListView.as_view(), name='planned-trips'),
    path('planned-trips/<int:pk>', views.PlannedTripDetailView.as_view(), name='planned-trip-detail'),
]

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]