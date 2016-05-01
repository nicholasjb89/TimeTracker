from django.shortcuts import render
from django.views import generic
from .models import Room, Day, Event, ScheduledEvent

# Create your views here.

class GetUnscheduledEvents(generic.ListView):
    template_name = "foobar/GetUnscheduledEvents.html"
    model = Event

    def get_queryset(self):

        events = Event.objects.filter(f_scheduled=False)
        return events

class GetAllRooms(generic.ListView):
    template_name = "foobar/GetAllRooms.html"
    model = Room

    def get_queryset(self):
        rooms = Room.objects.all()
        return rooms


class GetRoomsScheduledEventsOnXDay(generic.ListView):
    template_name = "foobar/GetAllRooms.html"
    model = ScheduledEvent

    def get_queryset(self):
        #Get Day somehow from URL Router
        #Get Room somehow from URL Router

        #look at polls/urls and polls views. This will help in this part.

        roomsEvents = ScheduledEvent.objects.filter()
        # filter by Day & Room
        return roomsEvents








