# Generated by Django 2.0.3 on 2018-03-14 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Towns', '0003_auto_20180314_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtype',
            name='Slot',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
