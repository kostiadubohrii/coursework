# Generated by Django 4.2.3 on 2024-03-17 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_remove_productlogo_product_product_leftinstock_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='is_visible',
        ),
    ]