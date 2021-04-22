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
    ordering = ('id',)
