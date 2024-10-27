import re
from django.db import models
from django.contrib.auth.models import AbstractUser
from config.settings import STATIC_URL
from django.utils.functional import cached_property
from django.urls import reverse

def class_to_camel_case(cls):
   return '_'.join([word.lower() for word in re.findall(r'[A-Z][a-z]*', cls.__name__)])

class User(AbstractUser):
    ...
    

class AbstractSkill(models.Model):
    name = models.CharField(max_length=64)
    experience = models.FloatField()
    description = models.TextField()
    
    def get_absolute_url(self):
        return reverse(class_to_camel_case(self.__class__), kwargs={'pk': self.pk})
    
    @cached_property
    def icon(self):
        return f'{STATIC_URL}icons/{self.name.lower().replace(' ', '_').replace('.', '_')}.png'
    
    def description_template(self):
        folder = class_to_camel_case(self.__class__)
        file = self.name.lower().replace(' ','-').replace('.', '-')
        return f'{folder}/{file}.html'
    
    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True
    

class GeneralSkill(AbstractSkill):
    ...
    

class LibraryFramework(AbstractSkill):
    language = models.ForeignKey('Language', blank=True, null=True, related_name='libraries_frameworks', on_delete=models.SET_NULL)

class Language(AbstractSkill):
    ...
    

class Project(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField()
    start_date = models.DateField()
    stop_date = models.DateField(blank=True, null=True)
    libraries_frameworks = models.ManyToManyField('LibraryFramework', related_name='projects')
    description = models.TextField(default='')
    github_url = models.URLField(blank=True, null=True)
    
    def get_absolute_url(self):
            return reverse('project', kwargs={'pk': self.pk})
        
    @cached_property
    def icon(self):
        return f'{STATIC_URL}icons/{self.name.lower().replace(' ', '_').replace('.', '_')}.png'
    
    def description_template(self):
        file = self.name.lower().replace(' ','-').replace('.', '-')
        return f'project/{file}.html'
    
    def __str__(self):
        return self.name