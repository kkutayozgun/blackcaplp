# Generated by Django 2.2 on 2022-01-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeseo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='test', verbose_name='Deneme'),
        ),
    ]
