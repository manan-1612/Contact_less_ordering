# Generated by Django 4.1.5 on 2023-03-05 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_order_date_time_alter_order_amount_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order_food_mapping',
            new_name='OFmapping',
        ),
    ]
