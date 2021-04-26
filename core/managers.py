from django.db import models
from django.db.models import Count, Case, When, Value, CharField, ExpressionWrapper, F, Sum, FloatField, DecimalField


class CustomerManager(models.Manager):

    def actives(self):
        return self.filter(active=True)

    def total_customer_by_district(self):
        return self.values('district__name').annotate(
            counter=Count('*')
        ).values('district__name', 'counter')

    def total_customer_by_marital_status(self):
        return self.values('marital_status__name').annotate(
            counter=Count('*')
        ).values('marital_status__name', 'counter')


class SaleItemManager(models.Manager):

    def total_saled_by_customer_gender(self):
        return self.annotate(
            gender_description=Case(
                When(sale__customer__gender='M', then=Value('Male')),
                default=Value('Female'),
                output_field=CharField()
            )
        ).annotate(
            subtotal=ExpressionWrapper(F('product__sale_price') * F('quantity'), output_field=FloatField())
        ).values('gender_description').annotate(
            total=Sum(F('subtotal'))
        ).values('gender_description', 'total')

    def total_commission_by_employee(self):
        return self.annotate(
            subtotal=ExpressionWrapper(F('product__sale_price') * F('quantity'), output_field=FloatField())
        ).annotate(
            commission_group=ExpressionWrapper(
                F('subtotal') * F('product__product_group__commission_percentage') / Value(100),
                output_field=FloatField()
            )
        ).values('sale__employee__name').annotate(
            total=Sum('commission_group', output_field=FloatField())
        ).values('sale__employee__name', 'total')

    def subtotal(self, sale_item_id: int):
        result = self.filter(pk=sale_item_id).annotate(
            subtotal=ExpressionWrapper(F('quantity') * F('product__sale_price'), output_field=DecimalField())
        ).values('subtotal').first()
        if result is not None:
            return result.get('subtotal')
        return 0
