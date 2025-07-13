from django.db import models
from solo.models import SingletonModel

class WebsiteConfig(SingletonModel):
    name = models.CharField(max_length=64)
    description = models.TextField(default='Description here')
    maintenance_mode = models.BooleanField(default=False,
        help_text='Will prevent the site from being accessed by non-staff. The maintenance message will be displayed.'
    )
    maintenance_message = models.TextField(
        default="We're curreuntly under maintenance! Check back soon!"  
    )

    class Meta:
        verbose_name = 'configuration'


class WebsiteContact(models.Model):
    name = models.CharField(max_length=64)
    is_primary = models.BooleanField(default=False)

    class WebsiteContactTypeChoices(models.TextChoices):
        PHONE = 'phone', 'Phone'
        EMAIL = 'email', 'Email'
    

    type = models.CharField(choices=WebsiteContactTypeChoices.choices, max_length=32,
        help_text='The type of contact.'
    )
    contact = models.CharField(max_length=64,
        help_text='The actual contact information (phone number/email address).'
    )
    svg = models.TextField(blank=True, null=True,
        help_text='The HTML svg icon of the social.'
    )

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'


class WebsiteSocial(models.Model):
    name = models.CharField(max_length=64)
    
    svg = models.TextField(
        help_text='The HTML svg icon of the social.'
    )
    link = models.URLField(
        help_text='The link to the actual social page.'
    )

    _cache_key = 'website_socials'

    class Meta:
        verbose_name = 'social'
        verbose_name_plural = 'socials'