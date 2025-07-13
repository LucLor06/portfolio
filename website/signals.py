from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete
from django.core.cache import cache
from . import models
import logging

logger = logging.getLogger(__name__)

def clear_website_socials_cache():
    logger.debug('Clearing website socials cache')
    cache.delete(models.WebsiteSocial._cache_key)

@receiver([post_save, pre_delete], sender=models.WebsiteSocial)
def website_social_cache(sender, instance, **kwargs):
    clear_website_socials_cache()

def clear_website_contacts_cache():
    logger.debug('Clearing website contact cache')
    cache.delete('website_contacts')

@receiver([post_save, pre_delete], sender=models.WebsiteContact)
def website_contact_signal(sender, instance, **kwargs):
    clear_website_contacts_cache()