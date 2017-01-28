from django.conf import settings

def inventory(request):
    return {
        'inventory_name': settings.NAME,
        'DEBUG': settings.DEBUG
    }
