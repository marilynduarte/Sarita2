# Generated by Django 3.1 on 2021-10-28 04:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='fecha')),
                ('total', models.FloatField(blank=True, default=0.0, null=True, verbose_name='total')),
                ('efectivo', models.FloatField(blank=True, default=0.0, null=True, verbose_name='efectivo')),
                ('vuelto', models.FloatField(blank=True, default=0.0, null=True, verbose_name='vuelto')),
                ('vendedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'db_table': 'venta',
            },
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(max_length=50, verbose_name='Numero de lote')),
                ('cantidad', models.PositiveIntegerField(verbose_name='cantidad')),
                ('subtotal', models.FloatField(blank=True, default=0.0, null=True, verbose_name='subtotal')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.venta')),
            ],
            options={
                'verbose_name': 'Detalle de Venta ',
                'verbose_name_plural': 'Detalles de Ventas',
                'db_table': 'detalle_venta',
            },
        ),
    ]
