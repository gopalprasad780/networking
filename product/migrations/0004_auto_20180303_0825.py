# Generated by Django 2.0.1 on 2018-03-03 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20180212_0813'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
