# Generated by Django 5.1.7 on 2025-03-25 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagramhunt', '0013_wordscore_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordscore',
            name='slug',
            field=models.SlugField(default=1, editable=False, unique=True),
            preserve_default=False,
        ),
    ]
