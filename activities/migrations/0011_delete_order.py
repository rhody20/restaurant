# Generated by Django 4.1.5 on 2023-03-28 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0010_rename_date_order_create_remove_order_product_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]
