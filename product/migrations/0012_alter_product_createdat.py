# Generated by Django 4.0.4 on 2022-05-13 10:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_alter_product_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='CreatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 13, 10, 43, 2, 904089, tzinfo=utc)),
        ),
    ]