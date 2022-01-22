from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PageConfig(AppConfig):
    name = 'page'
    verbose_name = _("Anasayfa Grubu")
    verbose_name_plural = _("Anasayfa Grubu")
