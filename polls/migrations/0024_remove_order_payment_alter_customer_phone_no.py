# Generated by Django 4.1.5 on 2023-03-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_alter_customer_email_alter_customer_phone_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_no',
            field=models.CharField(max_length=10),
        ),
    ]
