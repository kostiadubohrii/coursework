# Generated by Django 4.0.6 on 2023-07-19 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0018_rename_mean_review_product_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='review',
            new_name='user_review',
        ),
    ]
