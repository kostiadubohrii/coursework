from django.db.models.signals import post_save,post_delete
from .models import Reviews, Product
from django.dispatch import receiver
from .views import updateMeanReview
        
@receiver(post_delete, sender=Reviews)
def delete_review(sender, instance, *args, **kwargs):
    updateMeanReview(instance.product.id)

@receiver(post_save, sender=Reviews)
def create_review(sender, instance, created, **kwargs):
    if created:
        updateMeanReview(instance.product.id)