from django import template
from tree_element.models import TreeElement
from django.db.models import Q
import itertools
from operator import itemgetter

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name):
    roots = TreeElement.objects.filter(parent=None, menu__name=menu_name)
    condition = Q()
    for i in roots:
        condition = condition \
                    | Q(parent__name=i.name) \
                    | Q(parent__parent__name=i.name) \
                    | Q(parent__parent__parent__name=i.name)
    all_elements = TreeElement.objects.filter(
            condition
           ).values('parent__name', 'name', 'url')
    print(all_elements)
    sorted_elements = sorted(all_elements, key=itemgetter('parent__name'))
    sorted_dictionary = {}
    for key, group in itertools.groupby(sorted_elements, key=lambda x: x['parent__name']):
        sorted_dictionary[key] = list(group)
    print(sorted_dictionary)
    return {'all_elements': all_elements, 'roots': roots, 'data': sorted_dictionary.items()}

