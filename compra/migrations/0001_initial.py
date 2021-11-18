# Generated by Django 3.1 on 2021-10-28 04:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha de emisión')),
                ('seriefactura', models.CharField(max_length=50, verbose_name='Numero de Serie')),
                ('dtefactura', models.PositiveIntegerField(default=None, verbose_name='Numero de DTE')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Total')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.proveedor')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
                'db_table': 'compra',
            },
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechavencimiento', models.DateField(verbose_name='Fecha de vencimiento')),
                ('lote', models.CharField(max_length=50, verbose_name='Numero de lote del producto')),
                ('cantidad', models.PositiveIntegerField(default=0, verbose_name='Cantidad')),
                ('precio_compra', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Precio de compra')),
                ('subtotal', models.PositiveIntegerField(default=0.0, verbose_name='subtotal')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.producto')),
            ],
            options={
                'verbose_name': 'Detalle de Compra',
                'verbose_name_plural': 'Detalle de Compras',
                'db_table': 'detalle_compra',
            },
        ),
    ]
