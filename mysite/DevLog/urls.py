from django.conf.urls import url

from . import views

app_name = 'DevLog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^logs', views.LogListView.as_view(), name='logs'),
]