# Generated by Django 4.0.6 on 2023-09-30 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_rename_review_product_meanreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='- Due to the developing, no description is added to products', null=True),
        ),
    ]