# Generated by Django 4.0.4 on 2022-05-10 10:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_picture_picturedata_alter_product_createdat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picture',
            field=models.CharField(blank=True, max_length=9999, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='CreatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 10, 26, 54, 385863, tzinfo=utc)),
        ),
    ]
