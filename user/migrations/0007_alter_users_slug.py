# Generated by Django 4.2.1 on 2023-11-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_users_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='slug',
            field=models.SlugField(default='users'),
        ),
    ]
