from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Log, Category
from django.utils import timezone

# Create your views here.

class IndexView(generic.ListView):
    template_name = "DevLog/index.html"
    model = Log
    #this is the variable name to use in templates
    context_object_name = "latest_log_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Log.objects.order_by('-date_time')[:2]



class DetailView(generic.DetailView):
    template_name = "DevLog/index.html"
    model = Log
    #this is the variable name to use in templates
    context_object_name = "latest_log"
