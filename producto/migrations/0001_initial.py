# Generated by Django 3.1.6 on 2021-02-14 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('negocio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=250)),
                ('descripcion', models.CharField(blank=True, max_length=250)),
                ('imagen', models.ImageField(blank=True, upload_to='')),
                ('cantidad', models.IntegerField()),
                ('precio', models.FloatField()),
                ('negocio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='negocio.negocio')),
            ],
        ),
    ]
