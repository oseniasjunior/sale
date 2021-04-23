from django.db.models import QuerySet, Q
from django_filters import filterset
from core import models

LIKE = 'icontains'


class NumberInFilter(filterset.BaseInFilter, filterset.NumberFilter):
    pass


class CityFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr=LIKE)
    state_name = filterset.CharFilter(field_name='state__name', lookup_expr=LIKE)

    class Meta:
        model = models.City
        fields = ['name', 'state_name']


class EmployeeFilter(filterset.FilterSet):
    start_salary = filterset.NumberFilter(field_name='salary', lookup_expr='gte')
    end_salary = filterset.NumberFilter(field_name='salary', lookup_expr='lte')
    salary_in = NumberInFilter(field_name='salary', lookup_expr='in')

    class Meta:
        model = models.Employee
        fields = ['start_salary', 'end_salary', 'salary_in']


class ProductFilter(filterset.FilterSet):
    product_or_group = filterset.CharFilter(method='filter_product_or_group')

    @staticmethod
    def filter_product_or_group(queryset: QuerySet, name, value):
        return queryset.filter(Q(name__icontains=value) | Q(product_group__name__icontains=value))

    class Meta:
        model = models.Product
        fields = ['product_or_group']
