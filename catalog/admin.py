from django.contrib import admin
from .models import Trip, Country, DayInstance, Redactor, PlannedTrip, PlanStatusUpdate
from django.contrib.sites.models import Site
# Register your models here.


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_redactor', 'display_country', 'duration_calc', 'completed')


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    pass


@admin.register(DayInstance)
class DayInstanceAdmin(admin.ModelAdmin):
    list_display = ('travel', 'title', 'duration_calc')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_code', 'country_name')


@admin.register(PlannedTrip)
class PlannedTripAdmin(admin.ModelAdmin):
    pass


@admin.register(PlanStatusUpdate)
class PlanStatusUpdateAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(Site)
class SiteAdmin(admin.ModelAdmin):
    fields = ('id', 'name', 'domain')
    readonly_fields = ('id',)
    list_display = ('id', 'name', 'domain')
    list_display_links = ('name',)
    search_fields = ('name', 'domain')
admin.site.register(Site, SiteAdmin)