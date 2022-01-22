from django.contrib import admin
from parler.admin import TranslatableAdmin
from page.models import Keywords, HomeSeo

SEO_FIELDS = ('seo_title', 'meta_description', 'meta_keywords')

admin.site.site_header = 'Black Cap'

admin.site.register(Keywords, TranslatableAdmin)


@admin.register(HomeSeo)
class HomeSeoAdmin(TranslatableAdmin):
    pass
    # fields = SEO_FIELDS


