from django.contrib import admin
from .models import *

class TicketAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'event', 'rang', 'quantite')
    list_filter = ('event', 'rang')
    search_fields = ('name', 'event__name')

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_debut', 'location')
    list_filter = ('date_debut',)
    search_fields = ('name', 'location')

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Event, EventAdmin)
