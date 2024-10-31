from django.shortcuts import render
from .models import LibraryFramework, Language, GeneralSkill, Project
from django.views.generic import TemplateView, DetailView


class Home(TemplateView):
    template_name = 'home.html'


class LibraryFrameworkDetail(DetailView):
    model = LibraryFramework
    template_name = 'library_framework/library-framework.html'
    slug_field = 'slug'
    context_object_name = 'library_framework'


class LanguageDetail(DetailView):
    model = Language
    template_name = 'language/language.html'
    slug_field = 'slug'
    context_object_name = 'language'


class ProjectDetail(DetailView):
    model = Project
    template_name = 'project/project.html'
    slug_field = 'slug'
    context_object_name = 'project'
