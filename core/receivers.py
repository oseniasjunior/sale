from django.db.models.signals import post_save
from django.dispatch import receiver
from core import models, actions


@receiver(post_save, sender=models.SaleItem, dispatch_uid='update_total_sale', weak=False)
def update_total_sale(**kwargs):
    actions.SaleItemActions.update_total_sale(sale_item=kwargs.get('instance'))
