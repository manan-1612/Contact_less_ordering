# Generated by Django 4.1.7 on 2023-03-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_alter_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
