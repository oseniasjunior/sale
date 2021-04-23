from django.db.models import ExpressionWrapper, F, FloatField, Sum, Value
from django.db.models.functions import Coalesce

from core import models


class SaleItemActions:
    @staticmethod
    def update_total_sale(sale_item: 'models.SaleItem'):
        result = models.SaleItem.objects.filter(
            sale=sale_item.sale
        ).annotate(
            subtotal=ExpressionWrapper(F('quantity') * F('product__sale_price'), output_field=FloatField())
        ).aggregate(total=Coalesce(Sum('subtotal', output_field=FloatField()), Value(0, output_field=FloatField())))

        sale = models.Sale.objects.get(pk=sale_item.sale.id)
        sale.total = result.get('total')
        sale.save()
