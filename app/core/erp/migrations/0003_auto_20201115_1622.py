# Generated by Django 3.1.2 on 2020-11-15 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_delete_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descripcion',
            new_name='desc',
        ),
    ]
