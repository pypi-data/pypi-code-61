# Generated by Django 2.1.2 on 2018-10-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellsfargo', '0018_auto_20181019_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='prequalificationrequest',
            name='customer_initiated',
            field=models.BooleanField(default=False, verbose_name='Check was deliberately initiated by customer action'),
        ),
    ]
