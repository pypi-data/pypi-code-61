# Generated by Django 2.2 on 2019-04-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellsfargo', '0028_auto_20190401_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='cacreditapp',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cajointcreditapp',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prequalificationrequest',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='uscreditapp',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usjointcreditapp',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
