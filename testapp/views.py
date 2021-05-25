# import timeit

from django.conf import settings
from django.views.generic import ListView, DetailView

from testapp.models import Event


class EventDetailsView(DetailView):
    """list all details about single event"""
    model = Event
    template_name = 'event_details.html'
    context_object_name = 'event'


class EventsListView(ListView):
    """list all events data"""
    model = Event
    template_name = 'events-list.html'
    context_object_name = 'events'

    paginate_by = 100
    ordering = 'date'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EventsListView, self).get_context_data()
        return context
