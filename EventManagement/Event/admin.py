from django.contrib import admin
from .models import EventUser, Event, Address, event_photo


class EventUserAdmin(admin.ModelAdmin):
    list_display = ("fname", "lname", "email")
    list_filter = ("fname", "lname", "email")
    search_fields = ("fname", "lname", "email", "mobile")


class EventAdmin(admin.ModelAdmin):
    list_display = ("service", "Max_Guest", "start_date", "end_date","payment_status")
    list_filter = ("service", "Max_Guest", "start_date", "end_date")
    search_fields = ("service", "Max_Guest", "start_date", "end_date")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("city", "address", "country", "pincode")
    list_filter = ("city", "address", "country", "pincode")
    search_fields = ("city", "address", "country", "pincode")


class Event_photo_admin(admin.ModelAdmin):
    list_display = "Event"


admin.site.register(EventUser, EventUserAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(event_photo)
