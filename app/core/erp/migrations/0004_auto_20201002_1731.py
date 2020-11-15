# Generated by Django 3.1.2 on 2020-10-02 23:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_auto_20201002_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['id'],
            },
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateField(default=datetime.datetime(2020, 10, 2, 17, 31, 36, 634021), verbose_name='Fecha_de_registro'),
        ),
        migrations.AddField(
            model_name='employee',
            name='categ',
            field=models.ManyToManyField(to='erp.Category'),
        ),
    ]
