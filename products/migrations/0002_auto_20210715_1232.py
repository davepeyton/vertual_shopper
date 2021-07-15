# Generated by Django 3.2.5 on 2021-07-15 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]