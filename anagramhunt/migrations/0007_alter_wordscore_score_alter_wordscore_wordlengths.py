# Generated by Django 5.1.7 on 2025-03-25 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagramhunt', '0006_wordscore_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordscore',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wordscore',
            name='wordlengths',
            field=models.CharField(choices=[('5', '5 length'), ('6', '6 length'), ('7', '7 length'), ('8', '8 length')], default='5'),
        ),
    ]
