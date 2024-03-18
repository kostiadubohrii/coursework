# Generated by Django 4.2.3 on 2024-03-17 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_reviewline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlogo',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='leftInStock',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='minimumAmount',
            field=models.IntegerField(blank=True, default=4, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='topUpAmount',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
        migrations.DeleteModel(
            name='ProductImage',
        ),
        migrations.DeleteModel(
            name='ProductLogo',
        ),
    ]