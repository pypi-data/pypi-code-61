# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-04 19:33
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=128, unique=True)),
                ('status', models.CharField(choices=[('new', 'Invoiced'), ('pending', 'Payment pending'), ('paid', 'Payment received'), ('canceled', 'Invoice canceled')], default='new', max_length=128)),
                ('date', models.DateField()),
                ('invoiced_entity', models.CharField(blank=True, max_length=128)),
                ('billing_address', models.TextField()),
                ('compound', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(blank=True, max_length=128)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_order', models.IntegerField()),
                ('reference', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=1024)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='invoices.Invoice')),
            ],
            options={
                'ordering': ('invoice', 'line_order'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='invoiceline',
            unique_together=set([('invoice', 'line_order')]),
        ),
    ]
