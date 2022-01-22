from django.db import models
from django.utils.translation import ugettext_lazy as _
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields


# Create your models here.

class Keywords(TranslatableModel):
    translations = TranslatedFields(
        keyword=models.CharField(_('Anahtar Kelime'), max_length=100)
    )

    class Meta:
        verbose_name = _('Anahtar Kelime')
        verbose_name_plural = _('Anahtar Kelimeler')

    def __str__(self):
        return self.keyword


seo_translations = dict(
    seo_title=models.CharField(_('SEO Başlığı:'), max_length=200, blank=True, null=True),
    meta_description=models.TextField(_('Meta Açıklaması:'), blank=True, null=True),
    meta_keywords=models.ManyToManyField(Keywords, verbose_name=_('Anahtar Kelimeler'), blank=True)
)


class HomeSeo(TranslatableModel):
    translations = TranslatedFields(
        **seo_translations
    )
    image = models.ImageField(_('Deneme'), upload_to='test', blank=True, null=True)

    class Meta:
        verbose_name = _('SEO Anasayfa')
        verbose_name_plural = _('SEO Anasayfa')

    def __str__(self):
        return str(self.pk)
