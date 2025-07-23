from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Language, Technology, Tool, Skill, Project

def home(request: HttpRequest):
    context = {
        'languages': Language.objects.all_cached(prefetch=['tags']),
        'technologies': Technology.objects.all_cached(prefetch=['tags']),
        'tools': Tool.objects.all_cached(prefetch=['tags']),
        'skills': Skill.objects.all_cached(prefetch=['tags']),
        'projects': Project.objects.all_cached(),
    }
    return render(request, 'home.html', context)

def robots_txt(request: HttpRequest):
    return HttpResponse(
        content_type='text/plain',
        content="""
        User-agent: *
        Allow: /
        """
        )