from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Log, Category, Subject
from django.utils import timezone
from django.http import HttpResponse
from django.core import serializers

# Defining a subject category view for json request
def subject(request, category_id):
    return HttpResponse(serializers.serialize('json', Subject.objects.filter(category=category_id), fields=('pk','name')))

# Create your views here.


class IndexView(generic.ListView):
    #Should display multiple graphs showcasing life long time tracking
    template_name = "DevLog/index.html"
    model = Category
    pass

class LogListView(generic.ListView):
    template_name = "DevLog/loglist.html"
    model = Log
    context_object_name = "master" #this is the variable name to use in templates

    def get_queryset(self):
        """Return the last twenty published questions."""
        return Log.objects.order_by('category', '-subject', '-date_time')[:20]

class ChartView(generic.ListView):
    template_name = "DevLog/chart.html"
    model = Log
    context_object_name = "master" # refNameForHTML

    def get_queryset(self):
        """Django SQL to get data."""
        logs = Log.objects.filter(category__name__contains="Development").order_by('date_time') # Get all Development logs, ordered by date_time
            # hours = Log.objects.filter for hours by distinct date... but I don't remember how to do this shit

        # foreach log in logs,
        # get hours per unique day
        # return { Date : Hours } to plot on graph Development

        sameDay = logs[0].date_time.day # set to first day
        hoursInSameDay = 0.0;
        graphPoints = {}
        # dictionary[newKey] = value;
        # 2,3,4,5,6

        labelList = []
        seriesList = []

        #seperate our list of logs into labels and series for graphing Labels: Unique day, Series: Total Hours
        for log in logs:
            # TODO: Fix this so instead of June 2nd and May 2nd both returning 2 for the key, have them return unique dates for unique keys
            if sameDay == log.date_time.day:
               hoursInSameDay += log.hours
            else:
                # graphPoints[sameDay] = hoursInSameDay
                labelList.append(sameDay) # submit label
                seriesList.append(hoursInSameDay) # submit series value
                sameDay = log.date_time.day # get next day
                hoursInSameDay = log.hours # reloop

        #graphPoints[sameDay] = hoursInSameDay
        labelList.append(sameDay) # submit last unique day
        seriesList.append(hoursInSameDay) # submit last unique series value
        print(labelList)
        graphPoints = {"labels":labelList, "series":seriesList}
        # myTubel = (labelList, seriesList)
        # print(graphPoints)
        return graphPoints
        # for log in logs:
        #     # TODO: Fix this so instead of June 2nd and May 2nd both returning 2 for the key, have them return unique dates for unique keys
        #     if sameDay == log.date_time.day:
        #        hoursInSameDay += log.hours
        #     else:
        #         graphPoints[sameDay] = hoursInSameDay # submit
        #         sameDay = log.date_time.day # get next day
        #         hoursInSameDay = log.hours # reloop
        #
        # graphPoints[sameDay] = hoursInSameDay # submit last unique day
        #
        #
        # return graphPoints #total hours on different days


class CategoryGraphView(generic.DetailView):
    #This would display total hours within each Cateogry across a graph
    pass

class SubjectView(generic.DetailView):
    #This would display total hours & total logs within given Subject
    pass


class DetailView(generic.DetailView):
    template_name = "DevLog/index.html"
    model = Log
    #this is the variable name to use in templates
    context_object_name = "latest_log"
