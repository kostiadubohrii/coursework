# Generated by Django 4.2.3 on 2023-07-17 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_product_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
    ]
