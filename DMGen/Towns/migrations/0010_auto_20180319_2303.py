# Generated by Django 2.0.3 on 2018-03-20 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Towns', '0009_shop_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='Inventory',
            field=models.ManyToManyField(blank=True, null=True, to='Towns.Item'),
        ),
    ]
