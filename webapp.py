from django.conf import settings

class Mini:

    def __init__(self):

        self.title = 'mini'
        if hasattr(settings, 'TITLE'):
            self.title = settings.TITLE
            
        self.company_long = 'UWA'
        if hasattr(settings, 'COMPANY_LONG'):
            self.company_long = settings.COMPANY_LONG
            
        self.company = 'UWA'
        if hasattr(settings, 'UWA'):
            self.company = settings.COMPANY
            
        self.address = None
        if hasattr(settings, 'ADDRESS'):
            self.address = settings.ADDRESS
        
        self.house_number = None
        if hasattr(settings, 'HOUSE_NUMBER'):
            self.house_number = settings.HOUSE_NUMBER
            
        self.city = None
        if hasattr(settings, 'CITY'):
            self.city = settings.CITY
            
        self.province = None
        if hasattr(settings, 'PROVINCE'):
            self.province = settings.PROVINCE
            
        self.postal_code = None
        if hasattr(settings, 'POSTAL_CODE'):
            self.postal_code = settings.POSTAL_CODE
            
        self.country = None
        if hasattr(settings, 'COUNTRY'):
            self.country = settings.COUNTRY
            
        self.email = None
        if hasattr(settings, 'EMAIL'):
            self.email = settings.EMAIL
            
        self.phone = None
        if hasattr(settings, 'PHONE'):
            self.phone = settings.PHONE
            
        self.services_email = None
        if hasattr(settings, 'SERVICES_EMAIL'):
            self.services_email = settings.SERVICES_EMAIL
            
        self.pec = None
        if hasattr(settings, 'PEC'):
            self.pec = settings.PEC
            
        self.tax_id = None
        if hasattr(settings, 'TAX_ID'):
            self.tax_id = settings.TAX_ID
            
        self.pers_id = None
        if hasattr(settings, 'PERS_ID'):
            self.pers_id = settings.PERS_ID
        
        self.mini_css_cdn='https://cdn.jsdelivr.net/gh/giacomorizzotti/mini@main/css/mini.min.css'
        self.mini_js_cdn='https://cdn.jsdelivr.net/gh/giacomorizzotti/mini@main/js/mini.js'
        
        self.mini_gdpr=False
        self.mini_gdpr_cdn='https://cdn.jsdelivr.net/gh/giacomorizzotti/mini@main/js/gdpr.js'
        self.mini_slider=False
        self.mini_slider_cdn='https://cdn.jsdelivr.net/gh/giacomorizzotti/mini@main/js/slider.js'
        self.mini_debug=False
        self.mini_debug_cdn='https://cdn.jsdelivr.net/gh/giacomorizzotti/mini@main/js/debug.js'
            
        self.logo_height = None
        if hasattr(settings, 'LOGO_HEIGHT'):
            self.logo_height = settings.LOGO_HEIGHT
            
        self.scroll_logo_height = None
        if hasattr(settings, 'SCROLL_LOGO_HEIGHT'):
            self.scroll_logo_height = settings.SCROLL_LOGO_HEIGHT

        self.main_color = None
        if hasattr(settings, 'MAIN_COLOR'):
            self.main_color = settings.MAIN_COLOR
        self.main_color_dark = None
        if hasattr(settings, 'MAIN_COLOR_DARK'):
            self.main_color_dark = settings.MAIN_COLOR_DARK
        self.second_color = None
        if hasattr(settings, 'SECOND_COLOR'):
            self.second_color = settings.SECOND_COLOR
        self.second_color_dark = None
        if hasattr(settings, 'SECOND_COLOR_DARK'):
            self.second_color_dark = settings.SECOND_COLOR_DARK
        self.third_color = None
        if hasattr(settings, 'THIRD_COLOR'):
            self.third_color = settings.THIRD_COLOR
        self.third_color_dark = None
        if hasattr(settings, 'THIRD_COLOR_DARK'):
            self.third_color_dark = settings.THIRD_COLOR_DARK
        self.fourth_color = None
        if hasattr(settings, 'FOURTH_COLOR'):
            self.fourth_color = settings.FOURTH_COLOR
        self.fourth_color_dark = None
        if hasattr(settings, 'FOURTH_COLOR_DARK'):
            self.fourth_color_dark = settings.FOURTH_COLOR_DARK
        self.link_color = None
        if hasattr(settings, 'LINK_COLOR'):
            self.link_color = settings.LINK_COLOR
        self.link_hover_color = None
        if hasattr(settings, 'LINK_HOVER_COLOR'):
            self.link_hover_color = settings.LINK_HOVER_COLOR
        self.success_color = None
        if hasattr(settings, 'SUCCESS_COLOR'):
            self.success_color = settings.SUCCESS_COLOR
        self.info_color = None
        if hasattr(settings, 'INFO_COLOR'):
            self.info_color = settings.INFO_COLOR
        self.warning_color = None
        if hasattr(settings, 'WARNING_COLOR'):
            self.warning_color = settings.WARNING_COLOR
        self.danger_color = None
        if hasattr(settings, 'DANGER_COLOR'):
            self.danger_color = settings.DANGER_COLOR
        self.gingerbread_color = None
        if hasattr(settings, 'GINGERBREAD_COLOR'):
            self.gingerbread_color = settings.GINGERBREAD_COLOR
        self.acid_green = None
        if hasattr(settings, 'ACID_GREEN_COLOR'):
            self.acid_green = settings.ACID_GREEN_COLOR
        self.pulse_color = None
        if hasattr(settings, 'PULSE_COLOR'):
            self.pulse_color = settings.PULSE_COLOR
        self.main_color_transparent = None
        if hasattr(settings, 'MAIN_COLOR_TRANSPARENT'):
            self.main_color_transparent = settings.MAIN_COLOR_TRANSPARENT
            
        self.theme_color = self.main_color
        if hasattr(settings, 'THEME_COLOR'):
            self.theme_color = settings.THEME_COLOR
            
        if hasattr(settings, 'MINI_CSS_CDN'):
            self.mini_css_cdn = settings.MINI_CSS_CDN
        if hasattr(settings, 'MINI_JS_CDN'):
            self.mini_js_cdn = settings.MINI_JS_CDN
            
        if hasattr(settings, 'MINI_GDPR'):
            self.mini_gdpr = settings.MINI_GDPR
        if hasattr(settings, 'MINI_GDPR_CDN'):
            self.mini_gdpr_cdn = settings.MINI_GDPR_CDN
        if hasattr(settings, 'MINI_SLIDER'):
            self.mini_slider = settings.MINI_GDPR
        if hasattr(settings, 'MINI_SLIDER_CDN'):
            self.mini_slider_cdn = settings.MINI_GDPR_CDN
        if hasattr(settings, 'MINI_DEBUG'):
            self.mini_debug = settings.MINI_GDPR
        if hasattr(settings, 'MINI_DEBUG_CDN'):
            self.mini_debug_cdn = settings.MINI_GDPR_CDN
        
        self.AOS = True

        self.colors = {}
        self.css_root_vars = {}
        
        if self.logo_height:
            self.css_root_vars['--logo-height'] = self.logo_height
        if self.scroll_logo_height:
            self.css_root_vars['--scroll-logo-height'] = self.scroll_logo_height
            
        if self.main_color:
            self.colors['main_color'] = self.main_color
            self.css_root_vars['--main-color'] = self.main_color
        if self.main_color_dark:
            self.colors['main_color_dark'] = self.main_color_dark
            self.css_root_vars['--main-color-dark'] = self.main_color_dark
        if self.second_color:
            self.colors['second_color'] = self.second_color
            self.css_root_vars['--second-color'] = self.second_color
        if self.second_color_dark:
            self.colors['second_color_dark'] = self.second_color_dark
            self.css_root_vars['--second-color-dark'] = self.second_color_dark
        if self.third_color:
            self.colors['third_color'] = self.third_color
            self.css_root_vars['--third-color'] = self.third_color
        if self.third_color_dark:
            self.colors['third_color_dark'] = self.third_color_dark
            self.css_root_vars['--third-color-dark'] = self.third_color_dark
        if self.fourth_color:
            self.colors['fourth_color'] = self.fourth_color
            self.css_root_vars['--fourth-color'] = self.fourth_color
        if self.fourth_color_dark:
            self.colors['fourth_color_dark'] = self.fourth_color_dark
            self.css_root_vars['--fourth-color-dark'] = self.fourth_color_dark
        if self.link_color:
            self.colors['link_color'] = self.link_color
            self.css_root_vars['--link-color'] = self.link_color
        if self.link_hover_color:
            self.colors['link_hover_color'] = self.link_hover_color
            self.css_root_vars['--link-hover-color'] = self.link_hover_color
        if self.success_color:
            self.colors['success_color'] = self.success_color
            self.css_root_vars['--success'] = self.success_color
        if self.warning_color:
            self.colors['warning_color'] = self.warning_color
            self.css_root_vars['--warning'] = self.warning_color
        if self.danger_color:
            self.colors['danger_color'] = self.danger_color
            self.css_root_vars['--danger'] = self.danger_color
        if self.gingerbread_color:
            self.colors['gingerbread_color'] = self.gingerbread_color
            self.css_root_vars['--ginger-bread'] = self.gingerbread_color
        if self.acid_green:
            self.colors['acid_green'] = self.acid_green
        if self.pulse_color:
            self.colors['pulse_color'] = self.pulse_color
        if self.main_color_transparent:
            self.colors['main_color_transparent'] = self.main_color_transparent
            
            print('ciao')

    def get_title(self):
        return self.title
    def get_company_long(self):
        return self.company_long
    def get_company(self):
        return self.company
    def get_house_number(self):
        return self.house_number
    def get_city(self):
        return self.city
    def get_province(self):
        return self.province
    def get_postal_code(self):
        return self.postal_code
    def get_country(self):
        return self.country
    def get_email(self):
        return self.email
    def get_phone(self):
        return self.phone
    def get_services_email(self):
        return self.services_email
    def get_pec(self):
        return self.pec
    def get_tax_id(self):
        return self.tax_id
    def get_pers_id(self):
        return self.pers_id
    
    def get_mini_css_cdn(self):
        return self.mini_css_cdn
    def get_mini_js_cdn(self):
        return self.mini_js_cdn
    def get_mini_gdpr(self):
        return self.mini_gdpr
    def get_mini_gdpr_cdn(self):
        return self.mini_gdpr_cdn
    def get_mini_slider(self):
        return self.mini_slider
    def get_mini_slider_cdn(self):
        return self.mini_slider_cdn
    def get_mini_debug(self):
        return self.mini_debug
    def get_mini_debug_cdn(self):
        return self.mini_debug_cdn
    
    def get_company_variables(self):
        company_variables = {
            'company':self.company,
            'company_long':self.company_long,
            'address':self.address,
            'house_number':self.house_number,
            'city':self.city,
            'province':self.province,
            'postal_code':self.postal_code,
            'country':self.country,
            'email':self.email,
            'phone':self.phone,
            'services_email':self.services_email,
            'pec':self.pec,
            'full_address':self.address,
            'address_line_1':str(self.address)+' '+str(self.house_number),
            'address_line_2':str(self.postal_code)+' '+str(self.city)+' ('+str(self.province)+')'+', '+str(self.country),
            'tax_id':self.tax_id,
            'pers_id':self.pers_id,
            'colors':self.colors
        }
        return company_variables
    
    def get_theme_variables(self):
        theme_variables = {
            'theme_color':self.theme_color,
        }
        return theme_variables
    
    def get_colors(self):
        colors = self.colors
        return colors
    
    def get_css_root_vars(self):
        return self.css_root_vars
    
    def get_cdn(self):
        return self.dev_cdn
    
    @staticmethod
    def basic_context(self, request, context):
        
        context['mini_css_cdn'] = self.get_mini_css_cdn()
        context['mini_js_cdn'] = self.get_mini_js_cdn()
        if self.get_mini_gdpr() is True:
            context['gdpr'] = True
            context['mini_gdpr_cdn'] = self.get_mini_gdpr_cdn()
        if self.get_mini_slider() is True:
            context['slider'] = True
            context['mini_slider_cdn'] = self.get_mini_slider_cdn()
        if self.get_mini_debug() is True:
            context['debug'] = True
            context['mini_debug_cdn'] = self.get_mini_debug_cdn()

        context['webapp_title'] = self.get_title()
        context['company_variables'] = self.get_company_variables()
        context['theme_variables'] = self.get_theme_variables()

        context['css_root_vars'] = self.get_css_root_vars()
        
        if self.main_color:
            context['theme_color'] = self.main_color

        if request.user.groups.filter(name = 'manager').exists():
            context['user_manager'] = True

        return context