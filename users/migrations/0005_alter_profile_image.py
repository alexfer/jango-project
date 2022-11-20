# Generated by Django 4.0 on 2022-11-19 19:10

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to=users.models.Profile.profile_directory_path),
        ),
    ]
