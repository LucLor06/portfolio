from django.core.cache import cache
from .models import LibraryFramework, Language, Project

def navigation_context(request):
    context = cache.get_or_set(
        'navigation_context',
        {
            'libraries_frameworks': LibraryFramework.objects.all(),
            'languages': Language.objects.all(),
            'projects': Project.objects.all()
        },
        86400
    )
    return context