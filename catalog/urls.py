from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('trips/', views.TripListView.as_view(), name='trips'),
    path('trips/<str:pk>', views.TripDetailView.as_view(), name='trip-detail'),
    path('writers/', views.RedactorListView.as_view(), name='redactors'),
    path('writers/<str:pk>', views.RedactorDetailView.as_view(), name='redactor-detail'),
    path('countries/', views.CountryListView.as_view(), name='countries'),
    path('countries/<str:pk>', views.CountryDetailView.as_view(), name='country-detail'),
]
