# Generated by Django 4.0.6 on 2023-07-14 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
