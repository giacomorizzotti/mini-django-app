import string, random
from datetime import datetime
from django.conf import settings
from .website import Website


try:
    mini = settings.MINI
except AttributeError as e:
    print(f"AttributeError: {e}")
    mini = Website()
    

def randomCode(n):
    
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))

def basicContext(request, context):
    
    context['mini_css_cdn'] = mini.get_mini_css_cdn()
    context['mini_js_cdn'] = mini.get_mini_js_cdn()
    if mini.get_mini_gdpr() is True:
        context['gdpr'] = True
        context['mini_gdpr_cdn'] = mini.get_mini_gdpr_cdn()
    if mini.get_mini_slider() is True:
        context['slider'] = True
        context['mini_slider_cdn'] = mini.get_mini_slider_cdn()
    if mini.get_mini_debug() is True:
        context['debug'] = True
        context['mini_debug_cdn'] = mini.get_mini_debug_cdn()

    gdpr_app = 'gdpr.apps.GdprConfig' in settings.INSTALLED_APPS
    context['gdpr_app'] = gdpr_app

    context['webapp_title'] = mini.get_title()
    context['company_variables'] = mini.get_company_variables()
    context['theme_variables'] = mini.get_theme_variables()

    context['css_root_vars'] = mini.get_css_root_vars()
    
    if mini.main_color:
        context['theme_color'] = mini.main_color

    if request.user.groups.filter(name = 'manager').exists():
        context['user_manager'] = True

    return context

class DateConverter:
    regex = '\d{4}-\d{1,2}-\d{1,2}'
    format = '%Y-%m-%d'

    def to_python(self, value):
        return datetime.strptime(value, self.format).date()

    def to_url(self, value):
        return value.strftime(self.format)  

