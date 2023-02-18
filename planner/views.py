from django.views import generic
from django.shortcuts import render
from .models import Event
from datetime import date, datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

# Create your views here.
class EventListView(generic.ListView):
    queryset = Event.objects.filter(status=1).order_by('-created_on')
    template_name = 'cal.html'

class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'calendar.html'
def home(request, year, month):
    name = "plan"
    return render(request,
                  'cal.html', {
        "name": name
                  }
                  )