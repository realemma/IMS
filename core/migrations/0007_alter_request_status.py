# Generated by Django 4.2.1 on 2023-10-31 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_request_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('uncompleted', 'uncompleted'), ('pending', 'pending'), ('rejected', 'rejected'), ('approved', 'approved')], default='uncompleted', max_length=50),
        ),
    ]