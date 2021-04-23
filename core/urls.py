from rest_framework.routers import DefaultRouter
from core import viewsets

routers = DefaultRouter()
routers.register('state', viewset=viewsets.StateViewSet)
routers.register('zone', viewset=viewsets.ZoneViewSet)
routers.register('city', viewset=viewsets.CityViewSet)
routers.register('district', viewset=viewsets.DistrictViewSet)
routers.register('department', viewset=viewsets.DepartmentViewSet)
routers.register('marital_status', viewset=viewsets.MaritalStatusViewSet)
routers.register('employee', viewset=viewsets.EmployeeViewSet)
routers.register('product_group', viewset=viewsets.ProductGroupViewSet)
routers.register('product', viewset=viewsets.ProductViewSet)
routers.register('supplier', viewset=viewsets.SupplierViewSet)

urlpatterns = routers.urls
