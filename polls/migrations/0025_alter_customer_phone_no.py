# Generated by Django 4.1.5 on 2023-03-30 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_remove_order_payment_alter_customer_phone_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(max_length=20),
        ),
    ]
