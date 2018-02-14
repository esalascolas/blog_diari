from django.contrib import admin
from .models import Trip, Country, DayInstance, Redactor
# Register your models here.


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_redactor', 'display_country', 'duration_calc')

@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    pass


@admin.register(DayInstance)
class DayInstanceAdmin(admin.ModelAdmin):
    list_display = ('travel', 'title', 'duration_calc')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_code', 'country_name')
