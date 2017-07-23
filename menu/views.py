from django.shortcuts import redirect, render_to_response, render
from django.views.generic import TemplateView
from .models import Menu
from tree_element.models import TreeElement
from django.core.exceptions import ObjectDoesNotExist


class MenuView(TemplateView):

    def get(self, request, *args, **kwargs):
        menus = Menu.objects.all()
        return render_to_response('menu/main.html', context={
            'menus': menus,
        })


class MenuDetailView(TemplateView):

    def get(self, request, *args, **kwargs):
        url = kwargs.get('page_url', None)
        try:
            url = '/{}/'.format(url)
            element = TreeElement.objects.get(url=url)
            return render_to_response('menu/tree_element.html', context={
                'element': element,
            })
        except ObjectDoesNotExist:
            return render_to_response('menu/tree_element.html', context={})
