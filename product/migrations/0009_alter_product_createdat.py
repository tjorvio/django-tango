# Generated by Django 4.0.4 on 2022-05-11 11:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_merge_20220511_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='CreatedAt',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 11, 11, 8, 26, 494177, tzinfo=utc)),
        ),
    ]
