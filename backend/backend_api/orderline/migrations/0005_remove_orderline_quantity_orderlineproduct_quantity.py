# Generated by Django 4.0.6 on 2023-09-29 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderline', '0004_rename_product_text_orderlineproduct_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderline',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderlineproduct',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
