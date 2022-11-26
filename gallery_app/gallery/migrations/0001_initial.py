# Generated by Django 4.1.2 on 2022-11-26 05:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='Фотографии')),
                ('description', models.CharField(blank=True, default=' ', max_length=300, null=True, verbose_name='Подпись')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_picture', to=settings.AUTH_USER_MODEL, verbose_name='Автор фотографии')),
            ],
        ),
    ]