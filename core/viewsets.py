from rest_framework import viewsets

from core import models, serializers, mixins, filters


class ViewSetBase(viewsets.ModelViewSet, mixins.ViewSetExpandMixin):

    def list(self, request, *args, **kwargs):
        self.make_queryset_expandable(request)
        return super(ViewSetBase, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.make_queryset_expandable(request)
        return super(ViewSetBase, self).retrieve(request, *args, **kwargs)


class StateViewSet(ViewSetBase):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer


class ZoneViewSet(ViewSetBase):
    queryset = models.Zone.objects.all()
    serializer_class = serializers.ZoneSerializer


class CityViewSet(ViewSetBase):
    queryset = models.City.objects.all()
    serializer_class = serializers.CitySerializer
    filter_class = filters.CityFilter
    ordering_fields = '__all__'
    ordering = ('-id',)


class DistrictViewSet(ViewSetBase):
    queryset = models.District.objects.all()
    serializer_class = serializers.DistrictSerializer
    filter_class = filters.CityFilter
    ordering_fields = '__all__'
    ordering = ('-id',)


class DepartmentViewSet(ViewSetBase):
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    # filter_class = filters.CityFilter
    ordering_fields = '__all__'
    ordering = ('-id',)


class MaritalStatusViewSet(ViewSetBase):
    queryset = models.MaritalStatus.objects.all()
    serializer_class = serializers.MaritalStatusSerializer
    # filter_class = filters.CityFilter
    ordering_fields = '__all__'
    ordering = ('-id',)


class EmployeeViewSet(ViewSetBase):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    filter_class = filters.EmployeeFilter
    ordering_fields = '__all__'
    ordering = ('-id',)


class ProductGroupViewSet(ViewSetBase):
    queryset = models.ProductGroup.objects.all()
    serializer_class = serializers.ProductGroupSerializer
    # filter_class = filters.EmployeeFilter
    ordering_fields = '__all__'
    ordering = ('-id',)


class ProductViewSet(ViewSetBase):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_class = filters.ProductFilter
    ordering_fields = '__all__'
    ordering = ('-id',)


class SupplierViewSet(ViewSetBase):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
    # filter_class = filters.EmployeeFilter
    ordering_fields = '__all__'
    ordering = ('-id',)
