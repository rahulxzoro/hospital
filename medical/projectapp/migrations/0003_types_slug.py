# Generated by Django 5.0.2 on 2024-02-27 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='types',
            name='slug',
            field=models.SlugField(default='1', max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
