from .models import WebsiteConfig
from django.shortcuts import render

class MaintenanceMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            return self.get_response(request)
        
        config = WebsiteConfig.get_solo()
        if config.maintenance_mode and not request.user.is_staff:
            return render(request, 'maintenance.html', context={'message': config.maintenance_message}, status=503)
        
        response = self.get_response(request)
        return response 