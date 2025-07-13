from .models import WebsiteSocial, WebsiteContact, WebsiteConfig, WebsiteFAQ
from django.core.cache import cache

def website(request):
    context = {
        'website': WebsiteConfig.get_solo(),
        'website_socials': cache.get_or_set(WebsiteSocial._cache_key, lambda: list(WebsiteSocial.objects.all()), None),
        'website_contacts': cache.get_or_set('website_contacts', lambda: list(WebsiteContact.objects.all()), None),
    }
    return context
