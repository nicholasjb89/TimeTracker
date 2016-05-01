from django.contrib import admin
from .models import Room, Day, Event, ScheduledEvent

# Register your models here.

admin.site.register(Room)
admin.site.register(Event)
admin.site.register(Day)
admin.site.register(ScheduledEvent)
