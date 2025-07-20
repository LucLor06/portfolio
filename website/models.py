from django.db import models
from solo.models import SingletonModel
from django.core.cache import cache


class CacheAllManager(models.Manager):
    def all(self, *args, **kwargs):
        return cache.get_or_set(f'{self.model.all_cache_key()}', lambda: super(CacheAllManager, self).all(*args, **kwargs), None)


class AbstractCacheAllModel(models.Model):
    objects = CacheAllManager()

    class Meta:
        abstract = True

    def save(self, *args, skip_all_cache_clear=False, **kwargs):
        if not skip_all_cache_clear:
            cache.delete(self.__class__.all_cache_key())
        return super().save(*args, **kwargs)
    
    def delete(self, *args, skip_all_cache_clear=False, **kwargs):
        if not skip_all_cache_clear:
            cache.delete(self.__class__.all_cache_key())
        return super().delete(*args, **kwargs)
    
    @classmethod
    def all_cache_key(cls):
        return f'{cls._meta.db_table}:all'
    

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


class WebsiteContact(AbstractCacheAllModel):
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


class WebsiteSocial(AbstractCacheAllModel):
    name = models.CharField(max_length=64)
    
    svg = models.TextField(
        help_text='The HTML svg icon of the social.'
    )
    link = models.URLField(
        help_text='The link to the actual social page.'
    )

    class Meta:
        verbose_name = 'social'
        verbose_name_plural = 'socials'