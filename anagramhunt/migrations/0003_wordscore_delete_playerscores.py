# Generated by Django 5.1.7 on 2025-03-24 23:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anagramhunt', '0002_playerscores'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WordScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wordgame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anagramhunt.anagramhunt')),
            ],
        ),
        migrations.DeleteModel(
            name='PlayerScores',
        ),
    ]
