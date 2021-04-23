from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers
from core import models


class SerializerBase(FlexFieldsModelSerializer, serializers.HyperlinkedModelSerializer):
    def get_field_names(self, declared_fields, info):
        fields = super(SerializerBase, self).get_field_names(declared_fields, info)
        fields.insert(0, 'id')
        return fields


class StateSerializer(SerializerBase):
    class Meta:
        model = models.State
        fields = '__all__'


class ZoneSerializer(SerializerBase):
    class Meta:
        model = models.Zone
        fields = '__all__'


class CitySerializer(SerializerBase):
    class Meta:
        model = models.City
        fields = '__all__'

    expandable_fields = {
        'state': (
            'core.StateSerializer',
            {'source': 'state', 'fields': ['id', 'url', 'name']}
        )
    }


class DistrictSerializer(SerializerBase):
    class Meta:
        model = models.District
        fields = '__all__'

    expandable_fields = {
        'city': (
            'core.CitySerializer',
            {'source': 'city', 'fields': ['id', 'url', 'name']}
        ),
        'zone': (
            'core.ZoneSerializer',
            {'source': 'zone', 'fields': ['id', 'url', 'name']}
        ),
    }


class DepartmentSerializer(SerializerBase):
    class Meta:
        model = models.Department
        fields = '__all__'


class MaritalStatusSerializer(SerializerBase):
    class Meta:
        model = models.MaritalStatus
        fields = '__all__'


class EmployeeSerializer(SerializerBase):
    class Meta:
        model = models.Employee
        fields = '__all__'


class ProductGroupSerializer(SerializerBase):
    class Meta:
        model = models.ProductGroup
        fields = '__all__'


class ProductSerializer(SerializerBase):
    class Meta:
        model = models.Product
        fields = '__all__'

    expandable_fields = {
        'product_group': (
            'core.ProductGroupSerializer',
            {'source': 'product_group', 'fields': ['id', 'url', 'name']}
        ),
    }


class SupplierSerializer(SerializerBase):
    class Meta:
        model = models.Supplier
        fields = '__all__'
