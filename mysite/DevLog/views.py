from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Log, Category, Subject
from django.utils import timezone

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
        """Return the last five published questions."""
        return Log.objects.order_by('category', '-subject', '-date_time')[:20]

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
