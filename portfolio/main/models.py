import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import STATIC_URL
from django.utils.functional import cached_property
from django.urls import reverse
from django.utils.text import slugify

def class_to_camel_case(cls):
   return '_'.join([word.lower() for word in re.findall(r'[A-Z][a-z]*', cls.__name__)])


class User(AbstractUser):
    ...


class AbstractModel(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(class_to_camel_case(self.__class__), kwargs={'slug': self.slug})

    @cached_property
    def icon(self):
        return f'{STATIC_URL}icons/{self.slug}.png'

    def description_template(self):
        folder = class_to_camel_case(self.__class__)
        file = self.slug
        return f'{folder}/{file}.html'


class AbstractSkill(AbstractModel):
    experience = models.FloatField()

    class Meta:
        abstract = True


class GeneralSkill(AbstractSkill):
    ...


class LibraryFramework(AbstractSkill):
    languages = models.ManyToManyField('Language', blank=True, related_name='libraries_frameworks')


class Language(AbstractSkill):
    def projects(self):
        return Project.objects.filter(libraries_frameworks__languages=self).distinct()


class Project(AbstractModel):
    url = models.URLField()
    start_date = models.DateField()
    stop_date = models.DateField(blank=True, null=True)
    libraries_frameworks = models.ManyToManyField('LibraryFramework', related_name='projects')
    github_url = models.URLField(blank=True, null=True)
