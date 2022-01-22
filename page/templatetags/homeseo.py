from django import template
from page.models import HomeSeo

register = template.Library()


@register.simple_tag
def get_home():
    return HomeSeo.objects.first()
