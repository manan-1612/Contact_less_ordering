# Generated by Django 4.1.7 on 2023-03-11 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_alter_customer_c_id_alter_customer_exit_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_food_mapping',
            name='order_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]