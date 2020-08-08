# Generated by Django 3.0.4 on 2020-04-20 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0208_auto_20200329_1719"),
    ]

    operations = [
        migrations.AddField(
            model_name="jednostka",
            name="kolejnosc",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterModelOptions(
            name="jednostka",
            options={
                "ordering": ["kolejnosc", "nazwa"],
                "verbose_name": "jednostka",
                "verbose_name_plural": "jednostki",
            },
        ),
    ]
