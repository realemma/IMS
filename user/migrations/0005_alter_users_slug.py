# Generated by Django 4.2.1 on 2023-11-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_user_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]