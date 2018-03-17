from django.urls import path
from . import views
from .sitemaps import *
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'trip': TripSitemap(),
    'redactor': RedactorSitemap(),
    'country': CountrySitemap(),
    'static': StaticSitemap(),
}


urlpatterns = [
    path('', views.index, name='index'),
    path('trips/', views.TripListView.as_view(), name='trips'),
    path('trips/<str:pk>', views.TripDetailView.as_view(), name='trip-detail'),
    path('writers/', views.RedactorListView.as_view(), name='redactors'),
    path('writers/<str:pk>', views.RedactorDetailView.as_view(), name='redactor-detail'),
    path('countries/', views.CountryListView.as_view(), name='countries'),
    path('countries/<str:pk>', views.CountryDetailView.as_view(), name='country-detail'),
]


urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]