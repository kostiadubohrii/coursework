# Generated by Django 4.2.3 on 2024-01-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orderline', '0007_alter_orderline_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]