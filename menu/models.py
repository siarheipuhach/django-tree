from django.db import models
from tree_element.models import TreeElement
# Create your models here.


class Menu(models.Model):

    name = models.CharField(max_length=30)
    root_folders = models.ManyToManyField(TreeElement, related_name='menu',  related_query_name="menu")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'
