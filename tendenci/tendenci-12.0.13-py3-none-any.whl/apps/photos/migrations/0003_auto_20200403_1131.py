# Generated by Django 2.2.10 on 2020-04-03 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20180315_0857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pool',
            options={'permissions': (('view_photopool', 'Can view photopool'),), 'verbose_name': 'pool', 'verbose_name_plural': 'pools'},
        ),
    ]
