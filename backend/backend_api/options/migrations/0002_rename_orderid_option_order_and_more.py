# Generated by Django 4.0.6 on 2023-09-15 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('options', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='option',
            old_name='orderId',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='option',
            old_name='productId',
            new_name='product',
        ),
    ]
