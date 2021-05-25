from django.urls import path
from testapp.views import EventsListView, EventDetailsView

urlpatterns = [
    path('', EventsListView.as_view(), name='events_list'),
    path('event/<slug:slug>', EventDetailsView.as_view(), name='event_details'),
]
