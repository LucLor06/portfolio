from django.shortcuts import render
from .models import LibraryFramework, Language, GeneralSkill, Project
from django.views.generic import TemplateView, DetailView


class NavigationContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'libraries_frameworks': LibraryFramework.objects.all(), 'languages': Language.objects.all(), 'projects': Project.objects.all()})
        return context


class Home(NavigationContextMixin, TemplateView):
    template_name = 'home.html'


class LibraryFrameworkDetail(NavigationContextMixin, DetailView):
    model = LibraryFramework
    template_name = 'library_framework/library-framework.html'
    slug_field = 'slug'
    context_object_name = 'library_framework'
    
    
class LanguageDetail(NavigationContextMixin, DetailView):
    model = Language
    template_name = 'language/language.html'
    slug_field = 'slug'
    context_object_name = 'language'
    
    
class ProjectDetail(NavigationContextMixin, DetailView):
    model = Project
    template_name = 'project/project.html'
    slug_field = 'slug'
    context_object_name = 'project'
    