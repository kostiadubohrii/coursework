# Generated by Django 4.0.6 on 2023-09-29 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_isloggedin_user_isonline'),
        ('products', '0021_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.RenameField(
            model_name='reviews',
            old_name='created_at',
            new_name='posted_on',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='user_review',
        ),
        migrations.AddField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='review',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
