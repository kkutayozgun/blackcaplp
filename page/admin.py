from django.contrib import admin
from parler.admin import TranslatableAdmin
from page.models import Keywords, HomeSeo, DijitalItem, ServicesItem, ReferencesImage

SEO_FIELDS = ('seo_title', 'meta_description', 'meta_keywords')

admin.site.site_header = 'Black Cap'

admin.site.register(Keywords, TranslatableAdmin)


@admin.register(HomeSeo)
class HomeSeoAdmin(TranslatableAdmin):
    pass
    # fields = SEO_FIELDS


@admin.register(DijitalItem)
class DijitalItemAdmin(TranslatableAdmin):
    pass

@admin.register(ServicesItem)
class ServicesItemAdmin(TranslatableAdmin):
    pass

@admin.register(ReferencesImage)
class ReferencesImageAdmin(admin.ModelAdmin):
    pass
