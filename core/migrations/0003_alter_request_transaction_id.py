# Generated by Django 4.2.1 on 2023-10-29 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_request_slug_alter_request_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='transaction_id',
            field=models.CharField(default='REQ001', max_length=50),
        ),
    ]
