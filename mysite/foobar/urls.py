from django.conf.urls import url

from . import views

app_name = 'foobar'
urlpatterns = [
    url(r'^$', views.GetUnscheduledEvents.as_view(), name='foobar'),
    url(r'^rooms$', views.GetAllRooms.as_view(),name='roombar'),
]

# url(r'^subject/(?P<category_id>\d*)/$', 'DevLog.views.subject', name='subject'), deprecated warning

