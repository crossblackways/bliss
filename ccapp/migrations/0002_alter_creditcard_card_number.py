# Generated by Django 5.1 on 2024-08-19 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='card_number',
            field=models.CharField(max_length=25),
        ),
    ]
