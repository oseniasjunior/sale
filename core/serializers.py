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
