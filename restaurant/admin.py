""" Admin site model registration for the app """


from django.contrib import admin
from restaurant.models import Booking, MenuItem


# Register your models here.
admin.site.register(Booking)
admin.site.register(MenuItem)
