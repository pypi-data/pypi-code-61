# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 01:21
from __future__ import unicode_literals

from django.db import migrations

def dodaj_nagrody(apps, schema_editor):
    for skrot, nazwa in [
        ("AW01", "Prezes Rady Ministrów"),
        ("AW02", "minister kierujący działami administracji rządowej"),
        ("AW03", "wydział PAN"),
        ("AW04", "komitet naukowy PAN"),
        ("AW05", "Fundacja na rzecz Nauki Polskiej"),
        ("AW06", "zagraniczne towarzystwo naukowe"),
        ("AW07", "organizacja międzynarodowa lub ogólnopolskie towarzystwo "
                 "naukowe o szczególnym prestiżu")
    ]:
        apps.get_model("bpp", "OrganPrzyznajacyNagrody").objects.create(
            skrot=skrot, nazwa=nazwa)


class Migration(migrations.Migration):

    dependencies = [
        ('bpp', '0099_nagrody'),
    ]

    operations = [
        migrations.RunPython(
            dodaj_nagrody,
            migrations.RunPython.noop),
    ]
