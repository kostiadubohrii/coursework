# Generated by Django 4.0.6 on 2023-09-19 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_order_items_remove_order_product_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='userId',
        ),
    ]