# Generated by Django 4.2.3 on 2024-03-24 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_isloggedin_user_isonline'),
        ('products', '0032_alter_product_category_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(default='', max_length=86),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='review',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
