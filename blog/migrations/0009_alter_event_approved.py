# Generated by Django 4.2 on 2024-01-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_event_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Approved'),
        ),
    ]
