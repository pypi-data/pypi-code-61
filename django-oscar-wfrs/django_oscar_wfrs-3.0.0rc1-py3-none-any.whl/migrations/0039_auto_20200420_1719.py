# Generated by Django 2.2.12 on 2020-04-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellsfargo', '0038_auto_20200415_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prequalificationresponse',
            name='status',
            field=models.CharField(choices=[('A', 'Pre-qualification Approved'), ('D', 'Pre-qualification Not Approved'), ('E', 'System Error'), ('M', 'Down for Maintenance')], max_length=10, verbose_name='Transaction Status'),
        ),
    ]
