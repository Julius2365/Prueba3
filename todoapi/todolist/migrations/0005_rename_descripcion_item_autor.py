# Generated by Django 4.2.6 on 2024-01-25 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_alter_item_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='descripcion',
            new_name='autor',
        ),
    ]
