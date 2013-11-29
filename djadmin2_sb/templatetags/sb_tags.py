from django import template
from django.conf import settings

import djadmin2


directory = getattr(settings, 'ADMIN2_THEME_DIRECTORY', 'djadmin2_sb')
register = template.Library()

@register.inclusion_tag(directory + '/menu.html')
def menu(permissions):
    ctx = djadmin2.default.get_index_kwargs()
    ctx['permissions'] = permissions
    return ctx
