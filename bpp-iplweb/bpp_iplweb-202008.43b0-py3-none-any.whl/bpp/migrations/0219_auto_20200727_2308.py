# Generated by Django 3.0.7 on 2020-07-27 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0218_auto_20200727_2307"),
    ]

    operations = [
        migrations.AlterField(
            model_name="grant",
            name="rok",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
