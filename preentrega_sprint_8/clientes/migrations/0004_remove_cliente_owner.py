# Generated by Django 4.0.6 on 2022-08-22 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_cliente_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='owner',
        ),
    ]
