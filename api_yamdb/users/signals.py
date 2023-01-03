from django.contrib.auth.tokens import default_token_generator
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import User


@receiver(post_save, sender=User, dispatch_uid='create_confirmation_code')
def create_confirmation_code(sender, instance, created, **kwargs):
    if created:
        confirmation_code = default_token_generator.make_token(instance)
        instance.confirmation_code = confirmation_code
        print(instance.confirmation_code)
        instance.save()
