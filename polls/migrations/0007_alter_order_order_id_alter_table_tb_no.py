# Generated by Django 4.1.7 on 2023-03-03 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_alter_table_tb_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='table',
            name='tb_no',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
