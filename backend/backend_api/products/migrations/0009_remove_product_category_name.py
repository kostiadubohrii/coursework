# Generated by Django 4.2.3 on 2023-07-17 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_category_name_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
    ]
