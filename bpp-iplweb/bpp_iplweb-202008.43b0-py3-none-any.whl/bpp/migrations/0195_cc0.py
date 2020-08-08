# Generated by Django 2.2.10 on 2020-02-17 21:34

from django.db import migrations


def forwards_func(apps, schema_editor):
    Licencja_OpenAccess = apps.get_model("bpp", "Licencja_OpenAccess")
    db_alias = schema_editor.connection.alias
    Licencja_OpenAccess.objects.using(db_alias).get_or_create(
        skrot="CC-ZERO",
        nazwa="Creative Commons - Universal - Przekazanie do Domeny Publicznej (CC0 1.0)",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("bpp", "0194_auto_20200213_2148"),
    ]

    operations = [migrations.RunPython(forwards_func)]
