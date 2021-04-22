from django_filters import filterset
from core import models

LIKE = 'icontains'


class CityFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)
    state_name = filterset.CharFilter(field_name='state__name', lookup_expr=LIKE)

    class Meta:
        model = models.City
        fields = ['name', 'state_name']
