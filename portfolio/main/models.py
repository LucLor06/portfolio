import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import STATIC_URL
from django.utils.functional import cached_property
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime


class User(AbstractUser):
    ...


class AbstractModel(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self) -> str:
        return reverse(self.__class__.name_to_kebab_case(), kwargs={'slug': self.slug})

    @cached_property
    def icon(self) -> str:
        return f'{STATIC_URL}icons/{self.slug}.png'

    def description_template(self) -> str:
        folder = self.__class__.name_to_snake_case()
        file = self.slug
        return f'{folder}/{file}.html'
    
    @classmethod
    def name_to_snake_case(cls):
        return '_'.join([word.lower() for word in re.findall(r'[A-Z][a-z]*', cls.__name__)])

    @classmethod
    def name_to_kebab_case(cls):
        return '-'.join([word.lower() for word in re.findall(r'[A-Z][a-z]*', cls.__name__)])


class AbstractSkillManager(models.Manager):
    def proficient(self):
        return self.filter(is_learning=False)
    
    def learning(self):
        return self.filter(is_learning=True)

class AbstractSkill(AbstractModel):
    is_learning = models.BooleanField(default=False)
    began_learning = models.DateField()
    
    objects = AbstractSkillManager()
    
    class Meta:
        abstract = True
        ordering = ['is_learning', 'began_learning']
    
    def years_of_experience(self) -> float:
        now = datetime.today().date()
        print(now)
        print(self.began_learning)
        years = round(((now - self.began_learning).days) / 365.25, 2)
        return years


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
