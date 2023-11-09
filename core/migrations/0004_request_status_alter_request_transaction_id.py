# Generated by Django 4.2.1 on 2023-10-29 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_request_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('uncom', 'uncom'), ('pending', 'pending'), ('rejected', 'rejected'), ('approved', 'approved')], default='uncom', max_length=50),
        ),
        migrations.AlterField(
            model_name='request',
            name='transaction_id',
            field=models.CharField(max_length=50),
        ),
    ]