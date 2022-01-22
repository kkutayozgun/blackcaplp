from django import template
from page.models import DijitalItem

register = template.Library()


@register.simple_tag
def get_dijital_list():
    return DijitalItem.objects.all()
