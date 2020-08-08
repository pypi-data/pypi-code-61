# Generated by Django 2.2.7 on 2020-01-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celeryui', '0002_django110_py3k'),
    ]

    operations = [
        migrations.RunSQL("""
        drop index if exists celeryui_report_uid_like;
        alter table celeryui_report alter column uid type uuid using uid::uuid;
        create index on celeryui_report(uid);
        """, None, [
            migrations.AlterField(
                model_name='Report',
                name='uuid',
                field=models.UUIDField(unique=True, editable=False, blank=True, db_index=True),
            ),
        ]),
    ]
