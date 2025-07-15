from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.templatetags.static import static
from django.utils.functional import cached_property
from django.utils import timezone


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
    

class ValidatedModelMixin(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, skip_validation=False, **kwargs):
        if not skip_validation:
            self.full_clean()
        
        return super().save(*args, **kwargs)


class Tag(AbstractNamedModel, ValidatedModelMixin):
    @property
    def css_class(self):
        return f'tag--{self.slug}'
    

class AbstractSkill(AbstractNamedModel, ValidatedModelMixin):
    began_learning = models.DateField(default=timezone.localdate)
    icon = models.TextField()

    class Meta:
        abstract = True
    
    @cached_property
    def years_of_experience(self):
        today = timezone.localdate()
        delta = today - self.began_learning
        return delta.days/365.25
    
    @cached_property
    def display_years_of_experience(self):
        if self.years_of_experience < 1:
            return '< 1'
        return str(round(self.years_of_experience, 1))
    

class Language(AbstractSkill):
    tags = models.ManyToManyField('main.Tag', blank=True, related_name='languages')

    static_dir = 'languages'


class Technology(AbstractSkill):
    tags = models.ManyToManyField('main.Tag', blank=True, related_name='technologies')

    static_dir = 'technologies'


class Tool(AbstractSkill):
    tags = models.ManyToManyField('main.Tag', blank=True, related_name='tools')

    static_dir = 'tools'


class Skill(AbstractSkill):
    tags = models.ManyToManyField('main.Tag', blank=True, related_name='skills')

    static_dir = 'skills'