from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', name='draw_menu')
def draw_menu(name):
    menu = MenuItem.objects.filter(menu__menu_name=name)
    if menu:
        return {'menu': menu}
    else:
        raise template.TemplateSyntaxError('Not Found')
