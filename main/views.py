from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Language, Technology, Tool, Skill, Project

def home(request: HttpRequest):
    context = {
        'languages': Language.objects.all(),
        'technologies': Technology.objects.all(),
        'tools': Tool.objects.all(),
        'skills': Skill.objects.all(),
        'projects': Project.objects.all(),
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