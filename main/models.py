from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class User(AbstractUser):
    ...


class AbstractNamedModel(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if slugify(self.name) != self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)