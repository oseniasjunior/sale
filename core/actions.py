from django.db.models import ExpressionWrapper, F, FloatField, Sum, Value
from django.db.models.functions import Coalesce

from core import models


class SaleItemActions:
    @staticmethod
    def update_total_sale(sale_item: 'models.SaleItem'):
        sale = models.Sale.objects.get(pk=sale_item.sale.id)
        sale.total += models.SaleItem.objects.subtotal(sale_item_id=sale_item.id)
        sale.save()
