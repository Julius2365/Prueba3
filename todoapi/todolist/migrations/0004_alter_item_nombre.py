# Generated by Django 4.2.6 on 2023-10-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_item_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
    ]
