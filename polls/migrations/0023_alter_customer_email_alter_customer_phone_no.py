# Generated by Django 4.1.5 on 2023-03-30 04:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_alter_customer_email_alter_customer_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(11)]),
        ),
    ]
