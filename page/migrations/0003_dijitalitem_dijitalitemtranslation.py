# Generated by Django 2.2 on 2022-01-22 19:47

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_homeseo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='DijitalItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='dijital', verbose_name='Görsel')),
            ],
            options={
                'verbose_name': 'Dijital Görseli',
                'verbose_name_plural': 'Dijital Görselleri',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='DijitalItemTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('text', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Yazı')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='page.DijitalItem')),
            ],
            options={
                'verbose_name': 'Dijital Görseli Translation',
                'db_table': 'page_dijitalitem_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
