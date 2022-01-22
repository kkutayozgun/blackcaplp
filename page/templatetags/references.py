from django import template
from page.models import ReferencesImage

register = template.Library()


@register.simple_tag
def get_references_list():
    return ReferencesImage.objects.all()
