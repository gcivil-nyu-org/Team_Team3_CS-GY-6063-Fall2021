import django_filters

from .models import Event
from datetime import timedelta
from django_filters import DateRangeFilter
from django.utils.timezone import now


def _truncate(dt):
  return dt.date()
class EventFilter(django_filters.FilterSet):
  BOROUGH_CHOICES = (
    ("Manhattan", "Manhattan"),
    ("Queens", "Queens"),
    ("Bronx", "Bronx"),
    ("Brooklyn", "Brooklyn"),
    ("Staten Island", "Staten Island"),
  )

  SPORT_CHOICES = (
    ("Baseball", "Baseball"),
    ("Basketball", "Basketball"),
    ("Bocce", "Bocce"),
    ("Cricket", "Cricket"),
    ("Flag Football", "Flag Football"),
    ("Football", "Football"),
    ("Frisbee", "Frisbee"),
    ("Handball", "Handball"),
    ("Hiking", "Hiking"),
    ("Hockey", "Hockey"),
    ("Kickball", "Kickball"),
    ("Lacrosse", "Lacrosse"),
    ("Netball", "Netball"),
    ("Rugby", "Rugby"),
    ("Softball", "Softball"),
    ("Tennis", "Tennis"),
    ("Volleyball", "Volleyball")
  )

  DATE_CHOICES = [
    ('today', 'Today'),
    ('tomorrow','Tomorrow'),
    ('week', 'This Week'),
    ('month', 'This month'),
    ('year', 'This year'),
  ]

  DATE_FILTERS = {
    'today': lambda qs, name: qs.filter(**{
        '%s__year' % name: now().year,
        '%s__month' % name: now().month,
        '%s__day' % name: now().day
    }),
    'tomorrow': lambda qs, name: qs.filter(**{
        '%s__year' % name: (now() + timedelta(days=1)).year,
        '%s__month' % name: (now() + timedelta(days=1)).month,
        '%s__day' % name: (now() + timedelta(days=1)).day,
    }),
    'week': lambda qs, name: qs.filter(**{
        '%s__gte' % name: _truncate(now() + timedelta(days=7)),
        '%s__lt' % name: _truncate(now() + timedelta(days=1)),
    }),
    'month': lambda qs, name: qs.filter(**{
        '%s__year' % name: now().year,
        '%s__month' % name: now().month
    }),
    'year': lambda qs, name: qs.filter(**{
        '%s__year' % name: now().year,
    }),
  }
  

  sport = django_filters.ChoiceFilter(choices=SPORT_CHOICES)
  borough = django_filters.ChoiceFilter(choices=BOROUGH_CHOICES)
  date_range = DateRangeFilter(field_name='date', choices=DATE_CHOICES, filters=DATE_FILTERS)


  class Meta:

    model = Event
    fields=['sport', 'borough', 'date_range']


