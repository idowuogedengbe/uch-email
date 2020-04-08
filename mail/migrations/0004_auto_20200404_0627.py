# Generated by Django 3.0.4 on 2020-04-04 05:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_application_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='date_applied',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='date_last_edited',
            field=models.DateTimeField(auto_now=True),
        ),
    ]