from .models import WebsiteSocial, WebsiteContact, WebsiteConfig
from django.core.cache import cache

def website(request):
    context = {
        'website': WebsiteConfig.get_solo(),
        'website_socials': WebsiteSocial.objects.all(),
        'website_contacts': WebsiteContact.objects.all(),
    }
    return context
