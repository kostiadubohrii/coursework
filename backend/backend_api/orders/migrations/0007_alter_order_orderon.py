# Generated by Django 4.2.3 on 2024-03-24 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_rename_user_order_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderOn',
            field=models.DateField(default=None),
        ),
    ]
