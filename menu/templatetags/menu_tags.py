from django import template

from ..models import Category

register = template.Library()


@register.filter
def menu_categories(arg):
    return Category.objects.prefetch_related('dish_set')
