# Generated by Django 4.1.5 on 2023-04-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0021_backend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backend',
            name='card_details',
            field=models.IntegerField(),
        ),
    ]
