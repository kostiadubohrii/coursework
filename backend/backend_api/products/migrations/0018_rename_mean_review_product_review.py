# Generated by Django 4.2.3 on 2023-07-18 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_reviews_remove_product_review_product_mean_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='mean_review',
            new_name='review',
        ),
    ]
