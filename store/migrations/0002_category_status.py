# Generated by Django 4.2.1 on 2023-10-28 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(default='active', max_length=50),
        ),
    ]
