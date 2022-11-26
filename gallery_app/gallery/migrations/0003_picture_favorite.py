# Generated by Django 4.1.2 on 2022-11-26 07:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0002_rename_gallery_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite_pics', to=settings.AUTH_USER_MODEL, verbose_name='Избранные фотографии'),
        ),
    ]