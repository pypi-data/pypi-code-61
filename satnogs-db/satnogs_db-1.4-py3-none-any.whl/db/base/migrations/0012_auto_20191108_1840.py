# Generated by Django 2.2.6 on 2019-11-08 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_transmitterentry_service'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transmitterentry',
            old_name='mode',
            new_name='downlink_mode',
        ),
    ]
