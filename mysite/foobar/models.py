from django.db import models

# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    f_scheduled = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Room(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Day(models.Model):
   startTime = models.DateTimeField()
   endTime = models.DateTimeField()

class ScheduledEvent(models.Model):
    eventStartTime = models.DateTimeField()
    eventID = models.ForeignKey(Event)
    roomID = models.ForeignKey(Room)
    dayID = models.ForeignKey(Day)

    def __str__(self):
        return self.eventID.title

# Front end
# On day 1, RoomA put a 45 minute event at 2pm