from django.contrib import admin
from . models import BusCompany,Bus,Bookings,Route,Driver


# Register your models here.

class BusCompanyAdmin(admin.ModelAdmin):
    list_display = ['name','location_district']

class BusAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_plate']
class RouteAdmin(admin.ModelAdmin):
    list_display = ['name', 'bus', 'start_location','end_location']

class DriverAdmin(admin.ModelAdmin):
    list_display = ['name', 'bus', 'email']

class BookingsAdmin(admin.ModelAdmin):
    list_display = ['route', 'bus', 'date']

admin.site.register(BusCompany, BusCompanyAdmin)
admin.site.register(Bus, BusAdmin)
admin.site.register(Route, RouteAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Bookings, BookingsAdmin)
