from django.conf import settings

def add_settings( request ):
    """Add some selected settings values to the context"""
    return {
        'settings': {            
            'STAGING':                  settings.STAGING,
            'MAPIT_URL':                settings.MAPIT_URL,
            'GOOGLE_ANALYTICS_ACCOUNT': settings.GOOGLE_ANALYTICS_ACCOUNT,
        }        
    }
