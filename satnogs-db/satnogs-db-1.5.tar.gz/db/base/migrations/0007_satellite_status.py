# Generated by Django 1.10.6 on 2017-05-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20170323_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='satellite',
            name='status',
            field=models.CharField(choices=[('alive', 'alive'), ('dead', 'dead'), ('re-entered', 're-entered')], default='alive', max_length=10),
        ),
    ]
