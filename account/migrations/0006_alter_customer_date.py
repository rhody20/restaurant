# Generated by Django 4.1.5 on 2023-03-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]