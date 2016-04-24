from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Log, Category, Subject
from django.utils import timezone
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime

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

        dateFormat = "%Y/%m/%d"\

        head = str(logs[0].date_time.year), str(logs[0].date_time.month), str(logs[0].date_time.day)
        tail = str(logs[len(logs)-1].date_time.year), str(logs[len(logs)-1].date_time.month), str(logs[len(logs)-1].date_time.day)
        start = datetime.strptime(head[0]+"/"+head[1]+"/"+head[2],dateFormat)
        end = datetime.strptime(tail[0]+"/"+tail[1]+"/"+tail[2],dateFormat)
        delta = end - start
        print(delta.days, "------------------------")

        hoursPerDay = []
        # labels = [range(delta.days-1)]
        labels = []
        for i in range(delta.days):
            hoursPerDay.append(0)
            labels.append(i+1)

        print(len(hoursPerDay))

        for log in logs:
            # find delta day for log
            # add hours to hoursPerDay[delta]

            date = str(log.date_time.year), str(log.date_time.month), str(log.date_time.day)
            dateDelta = datetime.strptime(date[0]+"/"+date[1]+"/"+date[2],dateFormat) - start

            if dateDelta.days == 0:
                print("First day: ")
                hoursPerDay[dateDelta.days] += log.hours
            else:
                print(dateDelta.days-1)
                hoursPerDay[dateDelta.days-1] += log.hours

        return {"labels": labels, "series": hoursPerDay}


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
