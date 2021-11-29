import django_filters
from .models import Event
from django_filters import DateRangeFilter

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
  
  sport = django_filters.ChoiceFilter(choices=SPORT_CHOICES)
  borough = django_filters.ChoiceFilter(choices=BOROUGH_CHOICES)
  date_range = DateRangeFilter(field_name='date')


  class Meta:

    model = Event
    fields=['sport', 'borough', 'date_range']


