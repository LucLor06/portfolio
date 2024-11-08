from django.shortcuts import render
from .models import LibraryFramework, Language, GeneralSkill, Project
from django.views.generic import TemplateView, DetailView


class Home(TemplateView):
    template_name = 'home.html'


class ItemDetail(DetailView):
    slug_field = 'slug'
    
    def get_context_object_name(self, obj):
        return self.model.name_to_snake_case()
    
    def get_template_names(self):
        return [f'{self.model.name_to_snake_case()}/{self.model.name_to_kebab_case()}.html']


class LibraryFrameworkDetail(ItemDetail):
    model = LibraryFramework


class LanguageDetail(ItemDetail):
    model = Language


class ProjectDetail(ItemDetail):
    model = Project