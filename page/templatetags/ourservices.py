from django import template
from page.models import ServicesItem

register = template.Library()


@register.simple_tag
def get_ourservices_list():
    return ServicesItem.objects.all()
