from django import template
from menu.models import Menu

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name):
    menus = Menu.objects.filter(name=menu_name)
    return {'menus': menus}

