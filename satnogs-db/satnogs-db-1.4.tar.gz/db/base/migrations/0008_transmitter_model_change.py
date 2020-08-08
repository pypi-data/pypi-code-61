# Generated by Django 1.11.11 on 2019-04-04 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.db.models import Max
import django.utils.timezone
import shortuuidfield.fields


def from_alive_to_status(apps, schema_editor):
    Transmitter = apps.get_model('base', 'Transmitter')
    Transmitter.objects.filter(alive=True).update(status='active')
    Transmitter.objects.filter(alive=False).update(status='inactive')

def reverse_from_alive_to_status(apps, schema_editor):
    Transmitter = apps.get_model('base', 'Transmitter')
    Transmitter.objects.filter(status='active').update(alive=True)
    Transmitter.objects.filter(status='inactive').update(alive=False)
    Transmitter.objects.filter(status='invalid').update(alive=False)

def mark_approved_as_reviewed(apps, schema_editor):
    Transmitter = apps.get_model('base', 'Transmitter')
    Transmitter.objects.filter(approved=True).update(reviewed=True)

def reverse_mark_approved_as_reviewed(apps, schema_editor):
    pass

def allow_latest(apps, schema_editor):
    pass

def keep_only_latest(apps, schema_editor):
    Transmitter = apps.get_model('base', 'Transmitter')
    uuids = set(Transmitter.objects.values_list('uuid', flat=True))
    for uuid in uuids:
        entries = Transmitter.objects.filter(uuid=uuid)
        if entries.count() > 1:
            created_max = entries.aggregate(Max('created'))['created__max']
            for entry in entries:
                if entry.created != created_max:
                    entry.delete()

class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0007_transmitter_rename'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transmitter',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('base.transmitterentry',),
        ),
        migrations.CreateModel(
            name='TransmitterSuggestion',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
                'permissions': (('approve', 'Can approve/reject transmitter suggestions'),),
            },
            bases=('base.transmitterentry',),
        ),
        migrations.AlterModelOptions(
            name='transmitterentry',
            options={'verbose_name_plural': 'Transmitter entries'},
        ),
        migrations.AddField(
            model_name='transmitterentry',
            name='citation',
            field=models.CharField(default='CITATION NEEDED - https://xkcd.com/285/', max_length=512),
        ),
        migrations.AddField(
            model_name='transmitterentry',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='transmitterentry',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='transmitterentry',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('invalid', 'invalid')], default='active', max_length=8),
        ),
        migrations.RunPython(from_alive_to_status, reverse_from_alive_to_status),
        migrations.RemoveField(
            model_name='transmitterentry',
            name='alive',
        ),
        migrations.AddField(
            model_name='transmitterentry',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transmitterentry',
            name='mode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transmitter_entries', to='base.Mode'),
        ),
        migrations.AlterField(
            model_name='transmitterentry',
            name='satellite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmitter_entries', to='base.Satellite'),
        ),
        migrations.AlterField(
            model_name='transmitterentry',
            name='uuid',
            field=shortuuidfield.fields.ShortUUIDField(blank=True, db_index=True, editable=False, max_length=22),
        ),
        migrations.AlterUniqueTogether(
            name='transmitterentry',
            unique_together=set([('uuid', 'created')]),
        ),
        migrations.RunPython(mark_approved_as_reviewed, reverse_mark_approved_as_reviewed),
        migrations.RunPython(allow_latest, keep_only_latest),
    ]
