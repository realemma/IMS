# Generated by Django 4.2.1 on 2023-10-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_request_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='slug',
            field=models.SlugField(default='REQ001', null=True),
        ),
    ]
