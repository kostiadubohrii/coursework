# Generated by Django 4.0.6 on 2023-07-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_is_active_product_isactive_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='Images/None/No0img.jpg', upload_to='Images/'),
        ),
    ]
