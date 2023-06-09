# Generated by Django 4.1.7 on 2023-02-28 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_customer_phone_no_alter_food_item_avg_review_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='food_item',
            name='id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.RemoveField(
            model_name='table',
            name='id',
        ),
        migrations.AlterField(
            model_name='customer',
            name='c_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='food_item',
            name='food_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='table',
            name='tb_no',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
