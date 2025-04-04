# Generated by Django 5.1.7 on 2025-04-05 17:48

import play2learn.storage_backends
import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Image must be 500px by 500px.', storage=play2learn.storage_backends.PublicMediaStorage(), upload_to='media/public/avatars/', validators=[users.models.validate_avatar]),
        ),
    ]
