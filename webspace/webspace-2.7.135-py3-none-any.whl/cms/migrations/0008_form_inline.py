# Generated by Django 3.0.7 on 2020-07-06 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20200706_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='inline',
            field=models.BooleanField(default=False),
        ),
    ]
