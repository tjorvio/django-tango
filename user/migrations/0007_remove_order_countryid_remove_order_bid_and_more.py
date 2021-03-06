# Generated by Django 4.0.4 on 2022-05-11 15:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='CountryID',
        ),
        migrations.RemoveField(
            model_name='order',
            name='bid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='card_cvc',
        ),
        migrations.RemoveField(
            model_name='order',
            name='card_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cardholder',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='expire_month',
        ),
        migrations.RemoveField(
            model_name='order',
            name='expire_year',
        ),
        migrations.RemoveField(
            model_name='order',
            name='full_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='zip',
        ),
        migrations.AlterField(
            model_name='order',
            name='buyer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.profile'),
        ),
        migrations.CreateModel(
            name='PaymentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardholder', models.CharField(max_length=255)),
                ('card_number', models.CharField(max_length=16)),
                ('expire_month', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('expire_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('card_cvc', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)])),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.bid')),
            ],
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('street_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zip', models.IntegerField()),
                ('CountryID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.country')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.billingaddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.paymentinfo'),
        ),
    ]
