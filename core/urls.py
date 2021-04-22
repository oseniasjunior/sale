from rest_framework.routers import DefaultRouter
from core import viewsets

routers = DefaultRouter()
routers.register('state', viewset=viewsets.StateViewSet)
routers.register('zone', viewset=viewsets.ZoneViewSet)
routers.register('city', viewset=viewsets.CityViewSet)

urlpatterns = routers.urls
