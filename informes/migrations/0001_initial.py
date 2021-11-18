# Generated by Django 3.1 on 2021-10-28 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformePorRango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_dev', models.CharField(choices=[('Compra', 'Compra'), ('Venta', 'Venta'), ('Existencias', 'Existencias')], default='Compra', max_length=15, verbose_name='Tipo de Informe')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha De Inicio')),
                ('fecha_limite', models.DateField(verbose_name='Fecha De Limite')),
                ('total_compras', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Total de Compras')),
                ('total_ventas', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Total Ventas')),
                ('exist', models.PositiveIntegerField(default=0, verbose_name='Existencias')),
            ],
            options={
                'verbose_name': 'Informe por Rango',
                'verbose_name_plural': 'Informe por Rangos',
                'db_table': 'informe_por_rango',
            },
        ),
        migrations.CreateModel(
            name='InformePorLote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.lote')),
            ],
            options={
                'verbose_name': 'Informe por Lote',
                'verbose_name_plural': 'Informe por Lotes',
                'db_table': 'informe_por_lote',
            },
        ),
    ]