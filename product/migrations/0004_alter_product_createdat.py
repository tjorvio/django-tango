# Generated by Django 4.0.4 on 2022-05-07 23:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='CreatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 7, 23, 29, 11, 789948, tzinfo=utc)),
        ),
    ]
