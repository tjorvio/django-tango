# Generated by Django 4.0.4 on 2022-05-05 22:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_product_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='CreatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 22, 12, 2, 475680, tzinfo=utc)),
        ),
    ]