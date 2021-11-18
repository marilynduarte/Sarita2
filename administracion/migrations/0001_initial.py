# Generated by Django 3.1 on 2021-10-28 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'db_table': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(max_length=50, verbose_name='Numero de lote del producto')),
                ('fechavencimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento')),
            ],
            options={
                'verbose_name': 'Lote',
                'verbose_name_plural': 'Lotes',
                'db_table': 'lote',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre completo')),
                ('direccion', models.CharField(max_length=80, verbose_name='direccion')),
                ('telefono', models.CharField(blank=True, max_length=8, null=True, verbose_name='telefono')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'proveedor',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre del producto')),
                ('precio_venta', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Precio de Venta')),
                ('existencia', models.PositiveIntegerField(default=0, verbose_name='Existencia')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'producto',
            },
        ),
        migrations.CreateModel(
            name='DetalleProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.CharField(max_length=50, verbose_name='Numero de lote del producto')),
                ('subexistencias', models.PositiveIntegerField(default=0, verbose_name='Existencia')),
                ('fechavencimiento', models.DateField(blank=True, null=True, verbose_name='Fecha de vencimiento')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.producto')),
            ],
            options={
                'verbose_name': 'Detalle de Producto',
                'verbose_name_plural': 'Detalle de Productos',
                'db_table': 'detalleproducto',
            },
        ),
    ]