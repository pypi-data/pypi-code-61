# Generated by Django 3.0.4 on 2020-03-29 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("raport_slotow", "0002_auto_20200316_2027"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="raportuczelniaewaluacjaview",
            options={
                "managed": False,
                "ordering": ("rekord__tytul_oryginalny", "autorzy__kolejnosc"),
            },
        ),
    ]
